import os
import sys
from datetime import datetime
from time import time
from pyrogram import Client, filters
from pyrogram.types import Message
from config import HNDLR, SUDO_USERS

# System Uptime
START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (
     ("Chủ nhật", 60 * 60 * 24 * 7),
     ("ngày", 60 * 60 * 24),
     ("giờ", 60*60),
     ("phút", 60),
     ("giây", 1),
 )


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else ""))
    return ", ".join(parts)

@Client.on_message(filters.command(["ping"], prefixes=f"{HNDLR}"))
async def ping(client, m: Message):
   start = time()
   current_time = datetime.utcnow()
   m_reply = await m.edit("Pinging...")
   delta_ping = time() - start
   await m_reply.edit("0% ▒▒▒▒▒▒▒▒▒▒")
   await m_reply.edit("20% ██▒▒▒▒▒▒▒▒")
   await m_reply.edit("40% ████▒▒▒▒▒▒")
   await m_reply.edit("60% ██████▒▒▒▒")
   await m_reply.edit("80% ████████▒▒")
   await m_reply.edit("100% ██████████")
   end = datetime.now()
   uptime_sec = (current_time - START_TIME).total_seconds()
   uptime = await _human_time_duration(int(uptime_sec))
   await m_reply.edit(f"**┞◈ 𝗣𝗼𝗻𝗴!! 🏓**\n**┞◈ Pinger**  - {delta_ping * 1000:.3f} ms \n**┞◈ Uptime** - {uptime}")


@Client.on_message(filters.command(["pong"], prefixes=f"{HNDLR}"))
async def pong(client, m: Message):
   start = time()
   current_time = datetime.utcnow()
   pong = await m.edit("Pinging...")
   delta_ping = time() - start
   await pong.edit("❏◈===❏")
   await pong.edit("❏=◈==❏")
   await pong.edit("❏==◈=❏")
   await pong.edit("❏===◈❏")
   await pong.edit("❏==◈=❏")
   await pong.edit("❏=◈==❏")
   await pong.edit("❏◈===❏")
   await pong.edit("❏=◈==❏")
   await pong.edit("❏==◈=❏")
   await pong.edit("❏===◈❏")
   await pong.edit("❏==◈=❏")
   await pong.edit("❏=◈==❏")
   await pong.edit("❏◈===❏")
   await pong.edit("❏=◈==❏")
   await pong.edit("❏==◈=❏")
   await pong.edit("❏===◈❏")
   await pong.edit("❏===◈❏◈")
   await pong.edit("❏====❏◈◈")
   await pong.edit("**◈PINGGGG!**")
   end = datetime.now()
   uptime_sec = (current_time - START_TIME).total_seconds()
   uptime = await _human_time_duration(int(uptime_sec))
   await pong.edit(
       f"**❏ BOT ĐANG HOẠT ĐỘNG**\n**❏ Pinging** : {delta_ping * 1000:.3f} ms\n**❏ Bot Uptime** : {uptime}")

@Client.on_message(
    filters.user(SUDO_USERS) & filters.command(["restart"], prefixes=f"{HNDLR}")
)
async def restart(client, m: Message):
    await m.delete()
    loli = await m.reply("1")
    await loli.edit("2")
    await loli.edit("3")
    await loli.edit("4")
    await loli.edit("5")
    await loli.edit("6")
    await loli.edit("7")
    await loli.edit("8")
    await loli.edit("9")
    await loli.edit("**✅ Tgram đang khởi động lại**")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()


@Client.on_message(filters.command(["help"], prefixes=f"{HNDLR}"))
async def help(client, m: Message):
    await m.delete()
    HELP = f"""
 <b>👋 Hello {m.from_user.mention}!
 MENU TRỢ GIÚP NGƯỜI CHƠI NHẠC
 LỆNH CHO MỌI NGƯỜI
 • {HNDLR}play [song title |  youtube link |  reply audio file] - để phát nhạc
 • {HNDLR}videoplay [video title |  youtube link |  reply video file] - để phát video
 • {HNDLR}playlist - để xem danh sách phát
 • {HNDLR}ping - để kiểm tra trạng thái
 • {HNDLR}id - để xem id người dùng
 • {HNDLR}video - video title |  yt liên kết đến video tìm kiếm
 • {HNDLR}song - song title |  liên kết yt để tìm kiếm bài hát
 • {HNDLR}help - để xem danh sách các lệnh
 • {HNDLR}join- tham gia |  nhóm
 LỆNH CHO TẤT CẢ CÁC QUẢN TRỊ
 • {HNDLR}resume - để tiếp tục phát bài hát hoặc video
 • {HNDLR}pause - để tạm dừng phát một bài hát hoặc video
 • {HNDLR}skip - để bỏ qua một bài hát hoặc video
 • {HNDLR}end - để kết thúc phát lại
"""
    await m.reply(HELP)


@Client.on_message(filters.command(["repo"], prefixes=f"{HNDLR}"))
async def repo(client, m: Message):
    await m.delete()
    REPO = f"""
<b>👋 Hello {m.from_user.mention}!
🗃️ Người dùng chơi nhạc và video
🔰 Người dùng Telegram Khởi động để phát các bài hát và video trong cuộc trò chuyện thoại trên Telegram.
👩‍💻 Duy trì bởi
• Tgram.vn
📝 Yêu cầu
• Python 3.8+
• FFMPEG
• Nodejs v16+
[Tạo Bot Phát Nhạc](https://tgram.vn)
📝 Yêu cầu nhãn biến thể
• `API_ID` - Lấy từ [my.telegram.org](https://my.telegram.org)
• `API_HASH` - Lấy từ [my.telegram.org](https://my.telegram.org)
• `SESSION` - String session Pyrogram.
• `SUDO_USER` - ID tài khoản Telegram được sử dụng làm quản trị viên
• `HNDLR` - Xử lý để chạy userbot của bạn
"""
    await m.reply(REPO, disable_web_page_preview=True)
