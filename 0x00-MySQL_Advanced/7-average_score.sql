-- a SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student. Note: An average score can be a decimal
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

-- Create the stored procedure
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE total_score FLOAT;
    DECLARE projects_count INT;

    -- Compute the total score and count of projects for the user
    SELECT SUM(score), COUNT(*) INTO total_score, projects_count
    FROM corrections
    WHERE user_id = user_id;

    -- Compute and store the average score for the user
    UPDATE users
    SET average_score = IF(projects_count = 0, 0, total_score / projects_count)
    WHERE id = user_id;

    SELECT "Average score computed and stored.";
END //

DELIMITER ;
