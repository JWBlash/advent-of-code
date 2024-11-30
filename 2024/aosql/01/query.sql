SELECT
    c.name,
    w.wishes->>'first_choice' AS primary_wish,
    w.wishes->>'second_choice' AS backup_wish,
    w.wishes::jsonb->'colors'->>0 AS favorite_color,
    jsonb_array_length(w.wishes::jsonb->'colors') AS color_count,
    CASE
        WHEN t.difficulty_to_make = 1 THEN 'Simple Gift'
        WHEN t.difficulty_to_make = 2 THEN 'Moderate Gift'
        ELSE 'Complex Gift'
    END AS gift_complexity,
    CASE
        WHEN t.category = 'outdoor' THEN 'Outside Workshop'
        WHEN t.category = 'educational' THEN 'Learning Workshop'
        ELSE 'General Workshop'
    END AS workshop_assignment
FROM children c
JOIN wish_lists w ON c.child_id = w.child_id
JOIN toy_catalogue t ON toy_name = wishes->>'first_choice'
ORDER BY c.name ASC
LIMIT 5;
