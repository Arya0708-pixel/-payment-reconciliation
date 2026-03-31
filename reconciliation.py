import pandas as pd

def hybrid_reconcile(platform, bank):
    report = {}

    platform["date"] = pd.to_datetime(platform["date"])
    bank["settlement_date"] = pd.to_datetime(bank["settlement_date"])

    # 1) Exact ID matching via reference
    id_matches = bank.dropna(subset=["platform_ref"])
    id_matched_ids = set(id_matches["platform_ref"]).intersection(set(platform["id"]))
    report["id_matched"] = len(id_matched_ids)

    # 2) Fallback amount + date window (±2 days)
    unmatched_platform = platform[~platform["id"].isin(id_matched_ids)]
    amount_matches = 0

    for _, p in unmatched_platform.iterrows():
        window = bank[
            (bank["settlement_date"] >= p["date"] - pd.Timedelta(days=2)) &
            (bank["settlement_date"] <= p["date"] + pd.Timedelta(days=2))
        ]
        if any(round(p["amount"], 2) == round(b, 2) for b in window["amount"]):
            amount_matches += 1

    report["amount_window_matched"] = amount_matches

    # 3) Batch total comparison by day
    platform_daily = platform.groupby(platform["date"].dt.date)["amount"].sum()
    bank_daily = bank.groupby(bank["settlement_date"].dt.date)["amount"].sum()

    batch_diff = (platform_daily.sum() - bank_daily.sum()).round(2)
    report["batch_total_difference"] = batch_diff

    # Duplicates in bank
    report["bank_duplicates"] = bank.duplicated(subset=["amount", "settlement_date"]).sum()

    # Orphan refunds
    refunds = platform[platform["type"] == "refund"]
    orphan_refunds = refunds[~refunds["original_id"].isin(platform["id"])]
    report["orphan_refunds"] = len(orphan_refunds)

    return report