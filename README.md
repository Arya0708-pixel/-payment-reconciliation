Assumptions

The following assumptions were made to simulate a realistic payment reconciliation system:

Unique transaction IDs:
Each payment generated on the platform is assigned a unique transaction_id so that transactions can be tracked and matched correctly.
Delayed and batched bank settlements:
Bank settlements may take 1–2 days to appear and can be grouped into batches instead of being processed individually.
Different bank references:
The bank statement may not include the platform’s original transaction ID, as banks often generate their own reference numbers.
Refund linkage:
Every refund is assumed to be linked to a valid original transaction ID to ensure traceability and prevent invalid refunds.
Rounded bank amounts:
Bank transaction amounts are stored with two decimal precision, which can cause small rounding differences during reconciliation.
Single currency system:
All transactions are assumed to be in a single currency (e.g., INR), and foreign exchange conversions are not considered.