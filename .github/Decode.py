import os

def xor_decrypt(data, key):
    key_bytes = key.encode('utf-8')
    decrypted_bytes = bytearray()
    for i in range(len(data)):
        decrypted_bytes.append(data[i] ^ key_bytes[i % len(key_bytes)])
    return bytes(decrypted_bytes)

def main():
    file_path = os.path.join('output', 'chanels.txt')
    key = 'geaihua1980'
    
    # 读取加密文件内容
    with open(file_path, 'rb') as f:
        encrypted_content = f.read()
    
    # 解密文件内容
    decrypted_content = xor_decrypt(encrypted_content, key)
    
    # 将解密后的内容重新写入文件
    with open(file_path, 'wb') as f:
        f.write(decrypted_content)
        
if __name__ == '__main__':
    main()
