#legendsneverdie454@gmail.comprint(lol)
import random

class LudoGame:
    def __init__(self):
        self.players = ["Player 1", "Player 2", "Player 3", "Player 4"]
        self.positions = {player: [0, 0, 0, 0] for player in self.players}
        self.current_player = None

    def roll_dice(self):
        return random.randint(1, 6)

    def switch_player(self):
        current_index = self.players.index(self.current_player)
        next_index = (current_index + 1) % len(self.players)
        self.current_player = self.players[next_index]

    def move_piece(self, player, piece, steps):
        current_position = self.positions[player][piece]
        new_position = (current_position + steps) % 52  # Assuming a circular board with 52 positions
        self.positions[player][piece] = new_position

    def play_turn(self):
        print(f"{self.current_player}'s turn.")
        input("Press Enter to roll the dice...")

        steps = self.roll_dice()
        print(f"{self.current_player} rolled a {steps}.")

        # Implement logic for choosing a piece to move and updating its position
        # For simplicity, let's assume the player moves the first piece that can be moved
        for i, position in enumerate(self.positions[self.current_player]):
            if position != -1:  # -1 indicates a piece has reached the end
                self.move_piece(self.current_player, i, steps)
                break

    def check_winner(self):
        # Implement logic to check if any player has all pieces in the end
        for player, positions in self.positions.items():
            if all(position == -1 for position in positions):
                return player
        return None

    def play_game(self):
        self.current_player = random.choice(self.players)

        while True:
            self.play_turn()
            winner = self.check_winner()

            if winner:
                print(f"{winner} wins!")
                break

            self.switch_player()

if __name__ == "__main__":
    ludo_game = LudoGame()
    ludo_game.play_game()
