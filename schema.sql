CREATE TABLE
    IF NOT EXISTS segmento (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        corte_id INTEGER NOT NULL,
        tamanho_corte TEXT NOT NULL CHECK (tamanho IN ('P', 'M', 'G', 'GG')),
        x INTEGER NOT NULL,
        y INTEGER NOT NULL,
        width INTEGER NOT NULL,
        height INTEGER NOT NULL,
        FOREIGN KEY (bin) REFERENCES bin (id)
    );

CREATE TABLE
    IF NOT EXISTS bin (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sheet_width INTEGER NOT NULL,
        sheet_height INTEGER NOT NULL,
    );