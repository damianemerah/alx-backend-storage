-- creates a stored procedure AddBonus that adds a new correction for a student.
DROP PROCEDURE IF EXISTS AddBonus;

DELIMITER //

CREATE PROCEDURE AddBonus (IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
    DECLARE project_id INT;
    SET project_id = (SELECT id FROM projects WHERE name = project_name);

    -- if project doesn't exist, create it
    IF project_id IS NULL THEN
	INSERT INTO projects (name) VALUES (project_name);
	SET project_id = LAST_INSERT_ID();
    END IF;
    
    -- Insert the new correction
    INSERT INTO corrections (user_id, project_id, score)
    VALUES (user_id, project_id, score);

    -- Update the average score of the user
    UPDATE users
    SET average_score = (SELECT AVG(score) FROM corrections WHERE user_id = user_id)
    WHERE id = user_id;

    SELECT '--';
END //
