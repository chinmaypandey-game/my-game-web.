import pygame, random, asyncio

async def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 600))
    bird = pygame.Rect(50, 300, 30, 30)
    gravity, bird_move, pipes = 0.25, 0, []
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: bird_move = -6

        screen.fill((135, 206, 235))
        bird_move += gravity
        bird.y += bird_move
        pygame.draw.rect(screen, (255, 255, 0), bird)

        if len(pipes) == 0 or pipes[-1].x < 200:
            h = random.randint(150, 400)
            pipes.append(pygame.Rect(400, h, 50, 600))
            pipes.append(pygame.Rect(400, h - 750, 50, 600))

        for pipe in pipes[:]:
            pipe.x -= 3
            pygame.draw.rect(screen, (0, 200, 0), pipe)
            if bird.colliderect(pipe) or bird.top < 0 or bird.bottom > 600:
                bird.y, bird_move, pipes = 300, 0, []

        pygame.display.update()
        await asyncio.sleep(0)
        pygame.time.Clock().tick(60)

asyncio.run(main())
