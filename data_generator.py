import pandas as pd

def generate_data():
    platform = pd.DataFrame([
        ["P1", "2026-01-29", 100.00, "payment", None],
        ["P2", "2026-01-30", 33.335, "payment", None],
        ["P3", "2026-01-30", 33.335, "payment", None],
        ["P4", "2026-01-30", 33.335, "payment", None],
        ["P5", "2026-01-31", -20.00, "refund", "P0"],  # orphan refund
    ], columns=["id", "date", "amount", "type", "original_id"])

    bank = pd.DataFrame([
        ["B1", "2026-02-01", 100.00, "P1"],           # late settlement
        ["B2", "2026-01-31", 100.00, None],           # batched settlement
        ["B2_DUP", "2026-01-31", 100.00, None],       # duplicate
        ["B3", "2026-01-31", -20.00, "P999"],         # refund w/o original
    ], columns=["bank_id", "settlement_date", "amount", "platform_ref"])

    return platform, bank