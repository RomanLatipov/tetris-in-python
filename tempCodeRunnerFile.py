.key.get_pressed()     
    if key[pygame.K_UP] == True:
        rotation += 1
        if rotation == 4:
            rotation = 0
        block.rotation_state = rotation