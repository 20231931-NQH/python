import math


def chu_vi_hinh_tron(radius: float) -> float:
    if radius < 0:
        raise ValueError('Bán kính phải lớn hơn hoặc bằng 0')
    return 2 * math.pi * radius


def dien_tich_hinh_tron(radius: float) -> float:
    if radius < 0:
        raise ValueError('Bán kính phải lớn hơn hoặc bằng 0')
    return math.pi * radius ** 2


def chu_vi_hinh_chu_nhat(width: float, height: float) -> float:
    if width < 0 or height < 0:
        raise ValueError('Chiều rộng và chiều cao phải lớn hơn hoặc bằng 0')
    return 2 * (width + height)


def dien_tich_hinh_chu_nhat(width: float, height: float) -> float:
    if width < 0 or height < 0:
        raise ValueError('Chiều rộng và chiều cao phải lớn hơn hoặc bằng 0')
    return width * height
