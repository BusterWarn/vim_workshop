mod account;
mod transaction;

use account::BankAccount;
use transaction::{Transaction, TransactionType};

fn main() {
    // LSP features to try:
    // 1. Hover over BankAccount to see documentation
    // 2. Ctrl+click on BankAccount to go to definition
    let mut account = BankAccount::new("Alice", 1000.0);

    // 3. Code completion: Type 'account.' to see available methods
    account.display_balance();

    // 4. Hover over TransactionType to see enum variants
    let deposit = Transaction::new(
        TransactionType::Deposit,
        500.0,
        "Salary deposit".to_string(),
    );

    // 5. LSP will show error if you uncomment this (wrong type)
    // account.process_transaction("not_a_transaction");

    // 6. Go to definition on process_transaction
    account.process_transaction(deposit);

    // 7. LSP will warn about unused result
    let withdrawal = Transaction::new(
        TransactionType::Withdrawal,
        200.0,
        "ATM withdrawal".to_string(),
    );

    account.process_transaction(withdrawal);
    account.display_balance();
}

