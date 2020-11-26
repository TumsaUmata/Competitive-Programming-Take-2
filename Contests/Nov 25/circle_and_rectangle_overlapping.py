class Solution:
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        if x1 <= x_center <= x2 and y1 <= y_center <= y2:
            return True

        temp_x = x_center
        temp_y = y_center

        if x_center < x1:
            temp_x = x1
        elif x_center > x2:
            temp_x = x2

        if y_center < y1:
            temp_y = y1
        elif y_center > y2:
            temp_y = y2

        dx = x_center - temp_x
        dy = y_center - temp_y
        return (dx * dx + dy * dy) <= radius * radius
