from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import base64


def encrypt_cbc(
    data: str,
    secret_key: str,  # Base64 编码的密钥
    iv: str | None = None,  # Base64 编码的 IV，不传则随机生成
) -> str:
    """
    AES/CBC/PKCS5Padding 加密
    :param data: 明文数据
    :param secret_key: Base64 编码的密钥
    :param iv: Base64 编码的 IV，不传则随机生成
    :return: base64 编码的纯密文（不包含 IV）
    """
    # 1. 解码密钥和 IV（都是 Base64 编码）
    key_bytes = base64.b64decode(secret_key)
    if len(key_bytes) not in (16, 24, 32):
        raise ValueError("Key length must be 16, 24, or 32 bytes")

    if iv is not None:
        iv_bytes = base64.b64decode(iv)
        if len(iv_bytes) != 16:
            raise ValueError("IV must be 16 bytes after base64 decoding")
    else:
        iv_bytes = get_random_bytes(16)

    # 2. 创建 Cipher 对象
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv_bytes)

    # 3. 填充并加密
    padded_data = pad(data.encode("utf-8"), AES.block_size)
    encrypted_bytes = cipher.encrypt(padded_data)

    # 4. 只返回密文的 Base64（不拼接 IV）
    return base64.b64encode(encrypted_bytes).decode("ascii")


if __name__ == "__main__":
    key = "4GG54bEKD8vxEaaR"
    msg = "abcd@123"

    enc = encrypt_cbc(
        msg, secret_key="j4ul3NbWZcqGxOLZZamPVQ==", iv="wl1BtMOyipCKbKGcvlzDaw=="
    )
    print(f"密文: {enc}")


