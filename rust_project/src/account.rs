use crate::transaction::{Transaction, TransactionType};

/// Represents a bank account with basic operations
#[derive(Debug)]
pub struct BankAccount {
    holder: String,
    balance: f64,
    transactions: Vec<Transaction>,
}

impl BankAccount {
    /// Creates a new bank account
    ///
    /// # Arguments
    /// * `holder` - Name of the account holder
    /// * `initial_balance` - Initial deposit amount
    pub fn new(holder: &str, initial_balance: f64) -> Self {
        if initial_balance < 0.0 {
            panic!("Initial balance cannot be negative");
        }

        BankAccount {
            holder: holder.to_string(),
            balance: initial_balance,
            transactions: Vec::new(),
        }
    }

    /// Processes a transaction and updates the account balance
    pub fn process_transaction(&mut self, transaction: Transaction) -> Result<f64, String> {
        match transaction.transaction_type {
            TransactionType::Deposit => {
                self.balance += transaction.amount;
                self.transactions.push(transaction);
                Ok(self.balance)
            }
            TransactionType::Withdrawal => {
                if self.balance >= transaction.amount {
                    self.balance -= transaction.amount;
                    self.transactions.push(transaction);
                    Ok(self.balance)
                } else {
                    Err("Insufficient funds".to_string())
                }
            }
        }
    }

    /// Displays the current balance
    pub fn display_balance(&self) {
        println!(
            "Account holder: {}, Current balance: ${:.2}",
            self.holder, self.balance
        );
    }

    /// Returns the current balance
    pub fn get_balance(&self) -> f64 {
        self.balance
    }
}
