-- creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE user_id INT;
    DECLARE total_weighted_score FLOAT;
    DECLARE total_weight FLOAT;
    DECLARE current_score FLOAT;
    DECLARE current_weight INT;

    -- Declare a cursor to iterate through all users
    DECLARE user_cursor CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET @done = 1;

    -- Open the cursor
    OPEN user_cursor;

    -- Loop through all users
    user_loop: LOOP
        FETCH user_cursor INTO user_id;
        IF @done THEN
            LEAVE user_loop;
        END IF;

        SET total_weighted_score = 0;
        SET total_weight = 0;

        -- Calculate the total weighted score and total weight for the current user
        FOR c IN (SELECT score, weight FROM corrections WHERE user_id = user_id) DO
            SET current_score = c.score;
            SET current_weight = c.weight;
            SET total_weighted_score = total_weighted_score + (current_score * current_weight);
            SET total_weight = total_weight + current_weight;
        END FOR;

        -- Calculate the average weighted score for the current user
        IF total_weight > 0 THEN
            SET @average_weighted_score = total_weighted_score / total_weight;
        ELSE
            SET @average_weighted_score = 0;
        END IF;

        -- Update the user's average_score in the users table
        UPDATE users SET average_score = @average_weighted_score WHERE id = user_id;
    END LOOP;

    -- Close the cursor
    CLOSE user_cursor;
END //

DELIMITER ;
