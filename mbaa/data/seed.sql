-- Insert default expense categories
INSERT INTO categories (id, name, type) VALUES (UUID(),'food', 'expense'), (UUID(),'transportation', 'expense'), (UUID(),'entertainment', 'expense'), (UUID(),'health', 'expense'), (UUID(),'education', 'expense'), (UUID(),'gifts', 'expense'), (UUID(),'pets','expense'), (UUID(),'services','expense'), (UUID(),'job', 'budget'), (UUID(),'savings', 'pocket'), (UUID(),'freelance', 'budget'), (UUID(),'debt', 'expense');
