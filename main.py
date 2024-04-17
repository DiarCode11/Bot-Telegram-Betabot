import telepot
from telepot.loop import MessageLoop

# Fungsi untuk menangani pesan yang diterima
def handle_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    
    if content_type == 'text':
        # Jika pesan adalah teks, tanggapi dengan pesan yang sama
        bot.sendMessage(chat_id, msg['text'])
        print(msg['from']['id'])

# Token bot Telegram Anda
TOKEN = "7179267992:AAFPq0Gkt1rH92cPEWpS4wSr5oBvdJdhwzA"

# Membuat objek bot
bot = telepot.Bot(TOKEN)

# Mendengarkan pesan masuk
MessageLoop(bot, handle_message).run_as_thread()

# Menjalankan program untuk terus mendengarkan pesan
print('Bot sedang berjalan...')
while True:
    pass
