CREATE TABLE "pongcount"(
    "id" INTEGER NOT NULL,
    "count" INTEGER NOT NULL
);
ALTER TABLE
    "pongcount" ADD PRIMARY KEY("id");

INSERT INTO pongcount(id, count)
VALUES(1,0);