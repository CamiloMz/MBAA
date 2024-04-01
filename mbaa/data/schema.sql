USE mbaa;

-- Table for categories
CREATE TABLE categories (
    id CHAR(36) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    type ENUM('income', 'budget', 'expense', 'pocket') NOT NULL
);

-- Table for budgets
CREATE TABLE budgets (
    id CHAR(36) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    initial_amount DECIMAL(10, 2) NOT NULL,
    final_amount DECIMAL(10, 2) NOT NULL,
    date DATE NOT NULL,
    category_id CHAR(36) NULL,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);

-- Table for pockets
CREATE TABLE pockets (
    id CHAR(36) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    category_id CHAR(36) NULL,
    budget_id CHAR(36) NULL,
    description TEXT,
    FOREIGN KEY (category_id) REFERENCES categories(id),
    FOREIGN KEY (budget_id) REFERENCES budgets(id)
);

-- Table for expenses
CREATE TABLE expenses (
    id CHAR(36) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    start_date DATE NOT NULL,
    last_payment_date DATE NOT NULL,
    next_payment_date DATE NOT NULL,
    category_id CHAR(36) NULL,
    is_recurrent BOOLEAN NOT NULL,
    description TEXT,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);

-- Table for relation many-to-many between budgets and expenses
CREATE TABLE budgets_expenses (
    budget_id CHAR(36) NOT NULL,
    expense_id CHAR(36) NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (budget_id, expense_id),
    FOREIGN KEY (budget_id) REFERENCES budgets(id),
    FOREIGN KEY (expense_id) REFERENCES expenses(id)
);

-- Table for relation many-to-many between pockets and expenses
CREATE TABLE pockets_expenses (
    pocket_id CHAR(36) NOT NULL,
    expense_id CHAR(36) NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (pocket_id, expense_id),
    FOREIGN KEY (pocket_id) REFERENCES pockets(id),
    FOREIGN KEY (expense_id) REFERENCES expenses(id)
);


-- Intermediary table for many-to-many relationship between pockets and budgets
CREATE TABLE pockets_budgets (
    pocket_id CHAR(36) NOT NULL,
    budget_id CHAR(36) NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (pocket_id, budget_id),
    FOREIGN KEY (pocket_id) REFERENCES pockets(id),
    FOREIGN KEY (budget_id) REFERENCES budgets(id)
);