SELECT name, wishes -> 'first_choice' AS primary_wish
FROM wish_lists
JOIN children
ON children.child_id = wish_lists.child_id;
