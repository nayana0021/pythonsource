import pyautogui as p

# 메모장 가져오기
# w = p.getWindowsWithTitle("제목 없음")
# # 메모장 활성화
# w.activate()

# p.keyDown("shift")
# p.press("4")
# p.keyUp("4")

# p.keyDown("ctrl")
# p.keyDown("a")
# p.keyUp("a")
# p.keyUp("ctrl")

# 2 개 이상의 키보드 키 조합 시
# p.hotkey("ctrl","shift","esc")

# p.alert("자동화 수행에 실패했습니다.")
# p.alert(text="자동화 수행에 실패했습니다.", title="인증", button="OK")

# p.confirm(text="계속 진행하시겠습니까?", title="경고", buttons=["OK","Cancel"])

# p.prompt(text="아이디 입력", title="로그인", default="자동화")

p.password(text="비밀번호 입력", title="비밀번호")



