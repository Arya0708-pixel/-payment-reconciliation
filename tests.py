from data_generator import generate_data
from reconciliation import hybrid_reconcile

platform, bank = generate_data()
report = hybrid_reconcile(platform, bank)

assert report["id_matched"] == 1
assert report["bank_duplicates"] == 1
assert report["orphan_refunds"] == 1
assert report["batch_total_difference"] != 0

print("All reconciliation tests passed.")