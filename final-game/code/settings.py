import pygame, sys
from redbull import Redbull
from deadlines import Deadline
import random
import time


def actions(screen, programmer, redbulls):
    """configure movements of programmer and redbulls"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # moving
        elif event.type == pygame.KEYDOWN:
            # moving down
            if event.key == pygame.K_s:
                programmer.mdown = True
            # moving up
            elif event.key == pygame.K_w:
                programmer.mup = True
            elif event.key == pygame.K_SPACE:
                shot = Redbull(screen, programmer)
                redbulls.add(shot)
        # stop moving
        elif event.type == pygame.KEYUP:
            # moving down
            if event.key == pygame.K_s:
                programmer.mdown = False
            # moving up
            elif event.key == pygame.K_w:
                programmer.mup = False


def refresh_screen(bg_color, screen, logs, score, programmer, deadlines, redbulls):
    """refreshes screen"""
    screen.fill(bg_color)  # white, (0, 0, 0) for black
    score.show_score()
    for can in redbulls.sprites():
        can.materialize_redbull()  # placing redbulls on screen
    programmer.programmer()  # placing programmer on screen
    deadlines.draw(screen)  # placing deadlines on screen
    pygame.display.flip()  # updating screen


def remove_redbulls(screen, logs, score, deadlines, redbulls):
    """removing redbulls when exiting screen"""
    redbulls.update()
    for can in redbulls.copy():
        if can.rect.left >= 800:
            redbulls.remove(can)

        # if the number of red bulls is more than 15 at the same time, you die :(
        if len(redbulls) > 15:
            sys.exit()
    collisions = pygame.sprite.groupcollide(redbulls, deadlines, True, True)
    if collisions:
        logs.score += 3.5  # adding to score
        score.score_params()  # updating score

    if len(deadlines) == 0:
        redbulls.empty()
        create_session(screen, deadlines)


def update_session(logs, screen, programmer, deadlines, redbulls):
    """updating deadlines positions"""
    deadlines.update()
    if pygame.sprite.spritecollideany(programmer, deadlines):
        retake(logs, screen, programmer, deadlines, redbulls)
    death_check(logs, screen, programmer, deadlines, redbulls)


def create_session(screen, deadlines):
    """creating MANY deadlines"""
    deadline = Deadline(screen)
    deadline_width, deadline_height = deadline.rect.size

    # random number of rows and columns
    number_rows = random.randint(1, 8)
    number_deadlines_x = random.randint(1, 3)

    # creating deadlines matrix
    for row_number in range(number_rows):
        for deadline_number in range(number_deadlines_x):
            deadline = Deadline(screen)
            deadline.x = deadline_width + 2 * deadline_width * deadline_number + 500
            deadline.rect.x = deadline.x
            deadline.rect.y = deadline.rect.height + 2 * deadline.rect.height * row_number + 150
            deadlines.add(deadline)


def retake(logs, screen, programmer, deadlines, redbulls):
    """retaking an exam after deadline hits us"""
    if logs.lives_left > 0:
        logs.lives_left -= 1
        deadlines.empty()
        redbulls.empty()
        create_session(screen, deadlines)
        programmer.revive_programmer()
        time.sleep(1)
    else:
        logs.continue_game = False
        sys.exit()


def death_check(logs, screen, programmer, deadlines, redbulls):
    """checking if we die because the deadlines have come"""
    screen_edge = screen.get_rect()
    for exam in deadlines.sprites():
        if exam.rect.left <= screen_edge.left:
            retake(logs, screen, programmer, deadlines, redbulls)
            break
