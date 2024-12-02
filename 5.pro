% Facts about family relationships
father(john, mary).
father(john, mike).
mother(jane, mary).
mother(jane, mike).
father(mike, josh).
mother(susan, josh).

% A person is a parent if they are either a father or a mother.
parent(X, Y) :- father(X, Y).
parent(X, Y) :- mother(X, Y).

% A person is a sibling of another if they share the same parents.
sibling(X, Y) :- parent(P, X), parent(P, Y), X \= Y.

% A person is a grandparent if they are the parent of someone's parent.
grandparent(X, Y) :- parent(X, P), parent(P, Y).

% To test the queries:
% ?- parent(X, mary).
% ?- sibling(mike, X).
% ?- grandparent(X, josh).
