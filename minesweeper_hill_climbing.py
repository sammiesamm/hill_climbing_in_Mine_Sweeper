import numpy as np
import random

# Kích thước bảng
ROWS, COLS = 10, 10
MINES = 10

# Tạo bảng Minesweeper với mìn ngẫu nhiên
def generate_board(rows, cols, mines):
    board = np.zeros((rows, cols), dtype=int) # khởi tạo bảng
    mine_positions = random.sample(range(rows * cols), mines) # chọn vị trí mìn ngẫu nhiên

    for pos in mine_positions:
        r, c = divmod(pos, cols)
        board[r][c] = -1  # Đánh dấu ô có mìn
    
    # Cập nhật số lượng mìn xung quanh mỗi ô
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == -1:
                continue
            board[r][c] = sum(
                board[r+dr][c+dc] == -1
                for dr in [-1, 0, 1] if 0 <= r+dr < rows
                for dc in [-1, 0, 1] if 0 <= c+dc < cols
            )
    
    return board

# Tạo bảng trò chơi ngẫu nhiên
board = generate_board(ROWS, COLS, MINES)
solution_board = board.copy()  # Lưu lại bảng đáp án 


# Khởi tạo ma trận trạng thái (revealed) với giá trị False cho tất cả các ô (chưa mở)
revealed = np.zeros((ROWS, COLS), dtype=bool)

# Tính mật độ mìn toàn cục
GLOBAL_DENSITY = MINES / (ROWS * COLS)

# Hàm hiển thị bảng Minesweeper dựa trên hai ma trận: board và revealed
def display_board(board, revealed):
    for r in range(ROWS):
        row_display = []
        for c in range(COLS):
            if revealed[r][c]:
                row_display.append("M" if board[r][c] == -1 else str(board[r][c]))
            else:
                row_display.append("?")
        print("  ".join(row_display))
    print()

# Hàm heuristic tính toán mức độ rủi ro của ô ở vị trí (r, c)
def heuristic(board, revealed, r, c):
    # Nếu ô đã mở thì không được xem xét
    if revealed[r][c]:
        return float('inf') # gán cho nó một giá trị rủi ro vô cùng cao để loại ra khỏi quá trình lựa chọn.
    
    # nếu ô chưa mở
    risks = []
    # Xét tất cả các ô lân cận của ô (r, c)
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            nr, nc = r + dr, c + dc     # với mỗi ô lân cận (nr,nc)=(r+dr,c+dc) 
            if 0 <= nr < ROWS and 0 <= nc < COLS:   # nếu thuộc bảng
                # Nếu ô lân cận đã được mở và không phải mìn
                if revealed[nr][nc] and board[nr][nc] != -1:
                    number = board[nr][nc]
                    # Đếm số ô ẩn xung quanh ô số này (có thể chứa mìn)
                    hidden_count = 0
                    for r2 in range(nr - 1, nr + 2):
                        for c2 in range(nc - 1, nc + 2):
                            if 0 <= r2 < ROWS and 0 <= c2 < COLS:   # nếu thuộc bảng
                                if not revealed[r2][c2]:    # nếu ô chưa mở 
                                    hidden_count += 1
                    # Nếu có ô ẩn, ước tính rủi ro mà ô (r,c) góp phần vào ô số (nr, nc)
                    # (Chú ý: ở đây chưa có cơ chế gán cờ mìn nên ta cho flagged_count = 0)
                    if hidden_count > 0:
                        risk_estimate = number / hidden_count   # tính toán ước lượng rủi ro
                        risks.append(risk_estimate) # thêm vào danh sách risks[]
    # Nếu ô (r, c) không có ô số nào liền kề, sử dụng mật độ mìn toàn cục
    if not risks:   # danh sách risks vẫn trống (nghĩa là ô (r,c) không kề bất kỳ ô số nào đã mở) 
        return GLOBAL_DENSITY
    # kết luạn rủi ro bằng cách lấy trung bình các rủi ro ước lượnglượng
    return sum(risks) / len(risks)

def hill_climbing_minesweeper(board, revealed):
    game_lost = False  # Cờ để xác định xem có đạp mìn hay không
    while np.sum(revealed) < ROWS * COLS - MINES:
        best_cell = None
        min_risk = float('inf')
        for r in range(ROWS):
            for c in range(COLS):
                if not revealed[r][c]:
                    risk = heuristic(board, revealed, r, c)
                    if risk < min_risk:
                        min_risk = risk
                        best_cell = (r, c)
        if best_cell is None:
            break
        r, c = best_cell
        revealed[r][c] = True
        if board[r][c] == -1:
            print(f"Boom! Đã đạp trúng mìn tại ({r}, {c})!")
            display_board(board, revealed)
            game_lost = True
            break
        else:
            print(f"Mở ô ({r}, {c}) an toàn với rủi ro ước tính {min_risk:.4f}.")
            display_board(board, revealed)
    
    # Nếu chưa đạp mìn và đã mở hết các ô an toàn, thông báo thắng trò chơi
    if not game_lost:
        # Mở tất cả các ô chứa mìn (đánh dấu là "M")
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == -1:
                    revealed[r][c] = True
        print("Chúc mừng, bạn đã thắng trò chơi!")
        display_board(board, revealed)


hill_climbing_minesweeper(board, revealed)

# In ra bảng đáp án để so sánh
print("Bảng đáp án:")
print(solution_board)