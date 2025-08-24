import pygame

class MazeDisplay:
    def __init__(self, width=700, height=700):
        self.width = width
        self.height = height
        self.background_color = (255, 255, 255)  # White
        
    def initialize_display(self, title="Maze"):
        """Initialize pygame display"""
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(title)
        return self.screen
    
    def draw_grid(self, screen):
        """Draw the initial 20x20 grid with all walls"""
        screen.fill(self.background_color)
        
        # Draw a 20*20 grid, construct all walls (black lines)
        for i in range(21):
            pygame.draw.line(screen, (0, 0, 0), (0 + 50, 30 * i + 50), (600 + 50, 30 * i + 50), 1)
            pygame.draw.line(screen, (0, 0, 0), (30 * i + 50, 50), (30 * i + 50, 600 + 50), 1)
    
    def draw_maze(self, screen, removed_walls):
        """Draw complete maze with removed walls"""
        # First draw the grid
        self.draw_grid(screen)
        
        # Start and End points (erasing walls using white lines)
        pygame.draw.line(screen, (255, 255, 255), (50, 50), (50, 80), 2)
        pygame.draw.line(screen, (255, 255, 255), (650, 620), (650, 650), 2)
        
        # Remove walls based on stored data
        for wall_type, start_pos, end_pos in removed_walls:
            pygame.draw.line(screen, (255, 255, 255), start_pos, end_pos, 2)
    
    def draw_solution_path(self, screen, solution_path, vertex_positions):
        """Draw the solution path in red"""
        for i in range(len(solution_path) - 1):
            current_pos = vertex_positions[solution_path[i]]
            next_pos = vertex_positions[solution_path[i + 1]]
            pygame.draw.line(screen, (255, 0, 0), current_pos, next_pos, 3)
    
    def save_image(self, screen, filename):
        """Save current screen as image"""
        screenshot = pygame.Surface((self.width, self.height))
        screenshot.blit(screen, (0, 0))
        pygame.image.save(screenshot, filename)
