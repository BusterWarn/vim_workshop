/// Represents different types of banking transactions
#[derive(Debug, Clone)]
pub enum TransactionType {
    Deposit,
    Withdrawal,
}

/// Represents a bank transaction with its details
#[derive(Debug, Clone)]
pub struct Transaction {
    pub transaction_type: TransactionType,
    pub amount: f64,
    pub description: String,
}

impl Transaction {
    /// Creates a new transaction
    ///
    /// # Arguments
    /// * `transaction_type` - Type of transaction (Deposit or Withdrawal)
    /// * `amount` - Amount of money involved in the transaction
    /// * `description` - Description of the transaction
    pub fn new(transaction_type: TransactionType, amount: f64, description: String) -> Self {
        if amount <= 0.0 {
            panic!("Transaction amount must be positive");
        }

        Transaction {
            transaction_type,
            amount,
            description,
        }
    }
}
