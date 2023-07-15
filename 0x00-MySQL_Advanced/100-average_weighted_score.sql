-- creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_weighted_score FLOAT DEFAULT 0;
    DECLARE total_weight FLOAT DEFAULT 0;
    DECLARE current_score FLOAT;
    DECLARE current_weight INT;

    -- Calculate the total weighted score and total weight for the user
    FOR c IN (SELECT score, weight FROM corrections WHERE user_id = user_id) DO
        SET current_score = c.score;
        SET current_weight = c.weight;
        SET total_weighted_score = total_weighted_score + (current_score * current_weight);
        SET total_weight = total_weight + current_weight;
    END FOR;

    -- Calculate the average weighted score
    IF total_weight > 0 THEN
        SET @average_weighted_score = total_weighted_score / total_weight;
    ELSE
        SET @average_weighted_score = 0;
    END IF;

    -- Update the user's average_score in the users table
    UPDATE users SET average_score = @average_weighted_score WHERE id = user_id;
END //

DELIMITER ;
