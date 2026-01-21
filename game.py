# Game Tic Tac Toe
# Player 1 (X) vs Player 2 (O)

def print_board(board):
    """Menampilkan papan permainan"""
    print("\n")
    for i in range(3):
        print(f" {board[i][0]} | {board[i][1]} | {board[i][2]} ")
        if i < 2:
            print("-----------")
    print("\n")

def check_winner(board, player):
    """Mengecek apakah ada pemenang"""
    # Cek baris
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    # Cek kolom
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    # Cek diagonal
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    
    return False

def is_board_full(board):
    """Mengecek apakah papan sudah penuh"""
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def play_game():
    """Fungsi utama permainan"""
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    
    print("=" * 40)
    print("SELAMAT DATANG DI GAME TIC TAC TOE")
    print("=" * 40)
    print("\nPemain 1: X")
    print("Pemain 2: O")
    print("\nPosisi input (1-9):")
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 ")
    
    while True:
        print_board(board)
        print(f"Giliran Pemain {current_player}")
        
        while True:
            try:
                position = int(input(f"Pemain {current_player}, masukkan posisi (1-9): "))
                if position < 1 or position > 9:
                    print("❌ Input harus antara 1-9!")
                    continue
                
                row = (position - 1) // 3
                col = (position - 1) % 3
                
                if board[row][col] != ' ':
                    print("❌ Posisi sudah terisi! Coba posisi lain.")
                    continue
                
                board[row][col] = current_player
                break
            except ValueError:
                print("❌ Input tidak valid! Masukkan angka 1-9.")
        
        # Cek kemenangan
        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 PEMAIN {current_player} MENANG! 🎉")
            break
        
        # Cek draw
        if is_board_full(board):
            print_board(board)
            print("🤝 SERI! Permainan berakhir tanpa pemenang.")
            break
        
        # Ganti pemain
        current_player = 'O' if current_player == 'X' else 'X'

# Jalankan permainan
try:
    play_game()
except KeyboardInterrupt:
    print("\n\nPermainan dibatalkan. Terima kasih sudah bermain!")