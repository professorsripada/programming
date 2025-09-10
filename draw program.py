import pygame

# --- setup ---
pygame.init()
WIDTH, HEIGHT = 640, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Move the * with arrow keys (Q/Esc to quit)")
clock = pygame.time.Clock()

# asterisk setup
font = pygame.font.Font(None, 72)   # default font, size 72
star_surf = font.render("*", True, (0, 0, 0))  # black asterisk
star_rect = star_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2))

SPEED = 6  # pixels per frame

running = True
while running:
    # --- events ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key in (pygame.K_q, pygame.K_ESCAPE):
            running = False

    # --- movement (hold keys to move) ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        star_rect.x -= SPEED
    if keys[pygame.K_RIGHT]:
        star_rect.x += SPEED
    if keys[pygame.K_UP]:
        star_rect.y -= SPEED
    if keys[pygame.K_DOWN]:
        star_rect.y += SPEED

    # keep inside the window
    star_rect.clamp_ip(screen.get_rect())

    # --- draw ---
    screen.fill((255, 255, 255))  # white background
    screen.blit(star_surf, star_rect)
    pygame.display.flip()

    clock.tick(60)  # 60 FPS

pygame.quit()
