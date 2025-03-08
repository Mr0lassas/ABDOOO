import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# الحصول على مسار ChromeDriver من المستخدم
driver_path = input("ادخل مسار chromedriver (مثال: C:/path/to/chromedriver.exe): ")
driver = webdriver.Chrome(executable_path=driver_path)

def load_cookies(cookies):
    """
    تحميل الكوكيز المُدخلة يدويًا إلى المتصفح.
    """
    for cookie in cookies:
        # إزالة مفتاح 'expiry' إن وجد لتجنب مشاكل صلاحية الكوكيز
        if "expiry" in cookie:
            cookie.pop("expiry")
        driver.add_cookie(cookie)
    print("تم تحميل الكوكيز بنجاح.")

def login_with_cookies():
    """
    تسجيل الدخول إلى فيسبوك باستخدام الكوكيز المدخلة يدويًا.
    """
    driver.get("https://www.facebook.com/")
    time.sleep(3)
    # إدخال الكوكيز بصيغة JSON
    cookies_input = input("ادخل الكوكيز بصيغة JSON: ")
    try:
        cookies = json.loads(cookies_input)
    except Exception as e:
        print("خطأ في قراءة الكوكيز:", e)
        return False
    load_cookies(cookies)
    driver.refresh()
    time.sleep(5)
    print("تم تسجيل الدخول باستخدام الكوكيز.")
    return True

def navigate_to_group(group_url):
    """
    الانتقال إلى رابط القروب المُدخل.
    """
    driver.get(group_url)
    time.sleep(5)

def block_member(member_profile_url):
    """
    محاولة حظر عضو عبر الانتقال إلى صفحة البروفايل والضغط على عناصر الواجهة الخاصة بالحظر.
    قد تحتاج إلى تعديل محددات (XPath) العناصر بحسب التحديثات في واجهة فيسبوك.
    """
    driver.get(member_profile_url)
    time.sleep(3)
    try:
        # محاولة العثور على زر القائمة (قد يكون على شكل ثلاث نقاط أو أيقونة)
        menu_button = driver.find_element(By.XPATH, "//div[@aria-label='الإجراءات' or @aria-label='Action']")
        menu_button.click()
        time.sleep(2)
        
        # البحث عن خيار "حظر" بالنص المناسب (حسب لغة الواجهة)
        block_button = driver.find_element(By.XPATH, "//span[text()='حظر' or text()='Block']")
        block_button.click()
        time.sleep(2)
        
        # محاولة تأكيد الحظر في حالة ظهور نافذة تأكيد
        confirm_button = driver.find_element(By.XPATH, "//button/span[text()='تأكيد' or text()='Confirm']")
        confirm_button.click()
        time.sleep(2)
        
        print(f"تم حظر العضو: {member_profile_url}")
    except Exception as e:
        print(f"حدث خطأ أثناء محاولة حظر العضو {member_profile_url}: {e}")

def main():
    # تسجيل الدخول باستخدام الكوكيز
    if not login_with_cookies():
        driver.quit()
        return
    # إدخال رابط القروب يدويًا
    group_url = input("ادخل رابط القروب: ")
    navigate_to_group(group_url)
    
    # جمع روابط بروفايلات الأعضاء من الصفحة الحالية
    member_links = driver.find_elements(By.XPATH, "//a[contains(@href, 'facebook.com/profile.php') or contains(@href, 'facebook.com/')]")
    member_urls = list(set(link.get_attribute('href') for link in member_links))
    
    for url in member_urls:
        print("محاولة حظر العضو:", url)
        block_member(url)
        time.sleep(5)  # تأخير بسيط بين كل عملية حظر

if __name__ == "__main__":
    main()
    driver.quit()