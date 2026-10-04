from flask import Flask, request, Response
from datetime import date
from urllib.parse import quote
import math

app = Flask(__name__)

SITE_NAME = "احسبني"
SITE_URL = "https://ehsebni.com"


# =========================
# CSS المشترك
# =========================
# =========================
# CSS المشترك
# =========================
CSS = """
<style>

:root {
    --bg: #f5f5f7;
    --white: #ffffff;
    --text: #1d1d1f;
    --muted: #6e6e73;
    --blue: #0071e3;
    --blue-hover: #0077ed;
    --border: #d2d2d7;
    --soft-blue: #eef6ff;
    --shadow: 0 12px 35px rgba(0, 0, 0, 0.06);
    --shadow-hover: 0 22px 50px rgba(0, 0, 0, 0.10);
    --radius: 24px;
}

* {
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {
    margin: 0;
    font-family:
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        Tahoma,
        Arial,
        sans-serif;

    background:
        radial-gradient(
            circle at 50% -10%,
            rgba(0, 113, 227, 0.10),
            transparent 35%
        ),
        var(--bg);

    color: var(--text);
    line-height: 1.8;
    -webkit-font-smoothing: antialiased;
}


/* =========================
   الشريط العلوي
========================= */

header {
    position: sticky;
    top: 0;
    z-index: 1000;

    background: rgba(255, 255, 255, 0.78);

    backdrop-filter: blur(20px) saturate(180%);
    -webkit-backdrop-filter: blur(20px) saturate(180%);

    border-bottom: 1px solid rgba(0, 0, 0, 0.06);
}

.navbar {
    max-width: 1120px;
    margin: auto;

    min-height: 64px;
    padding: 12px 22px;

    display: flex;
    align-items: center;
    justify-content: space-between;

    gap: 25px;
}

.logo {
    color: var(--text);
    text-decoration: none;

    font-size: 23px;
    font-weight: 700;

    letter-spacing: -0.7px;

    white-space: nowrap;
}

.nav-links {
    display: flex;
    align-items: center;
    justify-content: center;

    gap: 20px;
    flex-wrap: wrap;
}

.nav-links a {
    color: #55555a;
    text-decoration: none;

    font-size: 14px;

    transition:
        color 0.2s ease,
        opacity 0.2s ease;
}

.nav-links a:hover {
    color: var(--blue);
}


/* =========================
   المحتوى
========================= */

.container {
    max-width: 1120px;

    margin: auto;

    padding:
        70px
        22px
        20px;
}


/* =========================
   القسم الرئيسي
========================= */

.hero {
    text-align: center;

    max-width: 850px;

    margin:
        0
        auto
        70px;
}

.hero h1 {
    margin: 0;

    font-size:
        clamp(
            46px,
            8vw,
            78px
        );

    line-height: 1.02;

    letter-spacing: -4px;

    font-weight: 750;
}

.hero h1::first-line {
    color: var(--text);
}

.hero p {
    max-width: 700px;

    margin:
        24px
        auto
        0;

    color: var(--muted);

    font-size: 20px;

    line-height: 1.7;
}


/* =========================
   بطاقات الحاسبات
========================= */

.tools {
    display: grid;

    grid-template-columns:
        repeat(
            3,
            minmax(0, 1fr)
        );

    gap: 20px;
}

.tool {
    position: relative;

    overflow: hidden;

    min-height: 290px;

    padding: 32px;

    background:
        rgba(
            255,
            255,
            255,
            0.86
        );

    border:
        1px solid
        rgba(0, 0, 0, 0.06);

    border-radius: var(--radius);

    box-shadow: var(--shadow);

    text-align: center;

    transition:
        transform 0.25s ease,
        box-shadow 0.25s ease;
}

.tool::after {
    content: "";

    position: absolute;

    width: 150px;
    height: 150px;

    border-radius: 50%;

    background:
        rgba(
            0,
            113,
            227,
            0.045
        );

    left: -70px;
    bottom: -75px;

    pointer-events: none;
}

.tool:hover {
    transform: translateY(-6px);

    box-shadow:
        var(--shadow-hover);
}

.icon {
    width: 62px;
    height: 62px;

    margin:
        0
        auto
        20px;

    display: flex;

    align-items: center;
    justify-content: center;

    border-radius: 19px;

    background: #f2f2f7;

    font-size: 30px;

    box-shadow:
        inset 0 0 0 1px
        rgba(0, 0, 0, 0.03);
}

.tool h2,
.tool h3 {
    margin:
        0
        0
        8px;

    font-size: 23px;

    letter-spacing: -0.5px;
}

.tool p {
    color: var(--muted);

    min-height: 58px;

    margin:
        0
        0
        20px;
}


/* =========================
   الأزرار
========================= */

.button {
    display: inline-flex;

    align-items: center;
    justify-content: center;

    min-height: 48px;

    padding:
        0
        22px;

    margin-top: 10px;

    background: var(--blue);

    color: white;

    text-decoration: none;

    border: none;

    border-radius: 999px;

    font-size: 15px;

    font-weight: 600;

    cursor: pointer;

    transition:
        background 0.2s ease,
        transform 0.2s ease,
        box-shadow 0.2s ease;
}

.button:hover {
    background: var(--blue-hover);

    transform:
        translateY(-1px);

    box-shadow:
        0 7px 18px
        rgba(0, 113, 227, 0.22);
}


/* =========================
   صفحات الحاسبات
========================= */

.card {
    max-width: 680px;

    margin:
        0
        auto
        45px;

    padding: 44px;

    background: var(--white);

    border:
        1px solid
        rgba(0, 0, 0, 0.06);

    border-radius: var(--radius);

    box-shadow: var(--shadow);
}

.card h1 {
    text-align: center;

    margin:
        0
        0
        12px;

    color: var(--text);

    font-size: 36px;

    letter-spacing: -1.3px;
}

.card h2 {
    color: var(--text);
}

.card > p:first-of-type {
    text-align: center;

    color: var(--muted);

    margin-bottom: 32px;
}


/* =========================
   الحقول
========================= */

label {
    display: block;

    margin:
        20px
        0
        8px;

    font-size: 14px;

    font-weight: 650;
}

input,
select,
textarea {
    width: 100%;

    padding:
        15px
        16px;

    border:
        1px solid
        var(--border);

    border-radius: 14px;

    background: #fff;

    color: var(--text);

    font-family: inherit;

    font-size: 16px;

    outline: none;

    transition:
        border-color 0.2s ease,
        box-shadow 0.2s ease;
}

input:focus,
select:focus,
textarea:focus {
    border-color:
        rgba(0, 113, 227, 0.65);

    box-shadow:
        0 0 0 4px
        rgba(0, 113, 227, 0.10);
}

textarea {
    min-height: 145px;

    resize: vertical;
}

button {
    width: 100%;

    margin-top: 15px;

    padding: 15px;

    border: none;

    border-radius: 999px;

    background: var(--blue);

    color: white;

    font-family: inherit;

    font-size: 17px;

    font-weight: 600;

    cursor: pointer;

    transition:
        background 0.2s ease,
        transform 0.2s ease;
}

button:hover {
    background: var(--blue-hover);

    transform:
        translateY(-1px);
}


/* =========================
   النتيجة
========================= */

.result {
    margin:
        30px
        0;

    padding:
        30px
        20px;

    background:
        linear-gradient(
            180deg,
            #f6fbff,
            #edf6ff
        );

    border:
        1px solid
        rgba(0, 113, 227, 0.10);

    border-radius: 22px;

    color: #174a78;

    text-align: center;

    font-size: 21px;

    line-height: 2.2;
}

.result strong {
    color: var(--text);

    font-size: 26px;
}


/* =========================
   المعلومات
========================= */

.info {
    max-width: 900px;

    margin:
        30px
        auto;

    padding: 36px;

    background:
        rgba(
            255,
            255,
            255,
            0.80
        );

    border:
        1px solid
        rgba(0, 0, 0, 0.06);

    border-radius: var(--radius);

    box-shadow:
        0 10px 30px
        rgba(0, 0, 0, 0.045);
}

.info h2 {
    margin-top: 0;

    color: var(--text);

    font-size: 28px;

    letter-spacing: -0.7px;
}

.info p {
    color: #4d4d52;
}

.back {
    display: block;

    text-align: center;

    margin-top: 20px;

    color: var(--blue);

    text-decoration: none;
}


/* =========================
   التذييل
========================= */

footer {
    margin-top: 80px;

    padding:
        42px
        20px
        52px;

    background:
        rgba(
            255,
            255,
            255,
            0.55
        );

    border-top:
        1px solid
        rgba(0, 0, 0, 0.07);

    text-align: center;

    color: #777;
}

.footer-links {
    margin-bottom: 12px;
}

.footer-links a {
    color: #666;

    text-decoration: none;

    margin:
        0
        8px;

    font-size: 14px;

    transition: color 0.2s ease;
}

.footer-links a:hover {
    color: var(--blue);
}


/* =========================
   الهاتف
========================= */

@media (max-width: 900px) {

    .tools {
        grid-template-columns:
            repeat(
                2,
                minmax(0, 1fr)
            );
    }

}


@media (max-width: 700px) {

    .navbar {
        flex-direction: column;

        padding:
            13px
            18px;

        gap: 10px;
    }

    .nav-links {
        gap:
            10px
            15px;
    }

    .container {
        padding:
            45px
            18px
            20px;
    }

    .hero {
        margin-bottom: 48px;
    }

    .hero h1 {
        font-size: 44px;

        letter-spacing: -2.5px;
    }

    .hero p {
        font-size: 17px;
    }

    .tools {
        grid-template-columns: 1fr;
    }

    .tool {
        min-height: auto;

        padding: 28px 23px;
    }

    .card,
    .info {
        padding:
            28px
            21px;

        border-radius: 21px;
    }

    .card h1 {
        font-size: 30px;
    }

}

</style>
"""


# =========================
# القالب العام
# =========================
def page(title, description, content):

    return f"""
    <!DOCTYPE html>

    <html lang="ar" dir="rtl">

    <head>
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-2278821232556257"
     crossorigin="anonymous"></script>
        <meta charset="UTF-8">
        <meta charset="UTF-8">

        <meta name="viewport"
              content="width=device-width, initial-scale=1.0">

        <title>{title}</title>

        <meta name="description"
              content="{description}">

        <meta name="robots"
              content="index, follow">

        <link rel="canonical"
              href="{SITE_URL}">

        {CSS}

    </head>

    <body>

        <header>

            <nav class="navbar">

                <a class="logo" href="/">
                    احسبني 🧮
                </a>

                <div class="nav-links">

                    <a href="/">الرئيسية</a>

                    <a href="/about">من نحن</a>

                    <a href="/contact">تواصل معنا</a>

                    <a href="/privacy">الخصوصية</a>

                    <a href="/terms">الشروط</a>

                </div>

            </nav>

        </header>

        <main class="container">

            {content}

        </main>

        <footer>

            <div class="footer-links">

                <a href="/about">من نحن</a>

                <a href="/contact">تواصل معنا</a>

                <a href="/privacy">سياسة الخصوصية</a>

                <a href="/terms">شروط الاستخدام</a>

            </div>

            ©️ 2026 احسبني - جميع الحقوق محفوظة

        </footer>

    </body>

    </html>
    """


# =========================
# الصفحة الرئيسية
# =========================
@app.route("/")
def home():

    content = """
    <section class="hero">

        <h1>احسبني 🧮</h1>

        <p>
            حاسبات وأدوات مجانية باللغة العربية تساعدك
            على إجراء الحسابات اليومية بسرعة وسهولة.
        </p>

    </section>

    <section class="tools">

        <div class="tool">

            <div class="icon">🎂</div>

            <h2>حاسبة العمر</h2>

            <p>
                احسب عمرك بدقة بالسنوات والأشهر والأيام.
            </p>

            <a class="button" href="/age">
                افتح الحاسبة
            </a>

        </div>


        <div class="tool">

            <div class="icon">📊</div>

            <h2>حاسبة النسبة المئوية</h2>

            <p>
                احسب قيمة نسبة مئوية من أي رقم بسهولة.
            </p>

            <a class="button" href="/percentage">
                افتح الحاسبة
            </a>

        </div>


        <div class="tool">

            <div class="icon">🏷️</div>

            <h2>حاسبة الخصم</h2>

            <p>
                احسب قيمة الخصم والسعر النهائي بعد التخفيض.
            </p>

            <a class="button" href="/discount">
                افتح الحاسبة
            </a>

        </div>


        <div class="tool">

            <div class="icon">💰</div>

            <h2>حاسبة القرض</h2>

            <p>
                احسب القسط الشهري وإجمالي المبلغ والفائدة.
            </p>

            <a class="button" href="/loan">
                افتح الحاسبة
            </a>

        </div>


        <div class="tool">

            <div class="icon">🔄</div>

            <h2>تحويل الوحدات</h2>

            <p>
                حوّل بين وحدات الطول والوزن ودرجة الحرارة.
            </p>

            <a class="button" href="/units">
                افتح الحاسبة
            </a>

        </div>


        <div class="tool">

            <div class="icon">⚖️</div>

            <h2>حاسبة مؤشر كتلة الجسم</h2>

            <p>
                احسب BMI باستخدام الوزن والطول.
            </p>

            <a class="button" href="/bmi">
                افتح الحاسبة
            </a>

        </div>

    </section>

    <section class="info">

        <h2>لماذا احسبني؟</h2>

        <p>
            صممنا احسبني ليكون مكانًا بسيطًا وسريعًا
            لإجراء الحسابات التي يحتاجها المستخدم في حياته اليومية.
            نركز على سهولة الاستخدام والنتائج الواضحة
            واللغة العربية.
        </p>

        <p>
            ستجد في الموقع أدوات للحسابات اليومية مثل العمر،
            النسب المئوية، الخصومات، القروض، تحويل الوحدات
            ومؤشر كتلة الجسم.
        </p>

    </section>
    """

    return page(
        "احسبني - حاسبات وأدوات مجانية",
        "احسبني موقع عربي مجاني يضم حاسبة العمر والنسبة المئوية والخصم والقرض وتحويل الوحدات ومؤشر كتلة الجسم.",
        content
    )


# =========================
# حاسبة العمر
# =========================
@app.route("/age", methods=["GET", "POST"])
def calculate_age():

    if request.method == "GET":

        content = """
        <div class="card">

            <h1>🎂 حاسبة العمر</h1>

            <p>
                أدخل تاريخ ميلادك لمعرفة عمرك بالسنوات
                والأشهر والأيام.
            </p>

            <form method="POST">

                <label>تاريخ الميلاد</label>

                <input
                    type="date"
                    name="birthdate"
                    required
                >

                <button type="submit">
                    احسب عمري
                </button>

            </form>

        </div>

        <section class="info">

            <h2>كيف تعمل حاسبة العمر؟</h2>

            <p>
                تعتمد الحاسبة على تاريخ الميلاد والتاريخ الحالي
                لحساب العمر بصورة مفهومة بالسنوات والأشهر والأيام.
            </p>

            <p>
                هذه الأداة مناسبة لمعرفة العمر الحالي بسرعة
                دون الحاجة إلى إجراء الحساب يدويًا.
            </p>

        </section>
        """

        return page(
            "حاسبة العمر - احسبني",
            "احسب عمرك بالسنوات والأشهر والأيام باستخدام حاسبة العمر المجانية من احسبني.",
            content
        )

    birthdate = request.form.get("birthdate")

    try:

        birth = date.fromisoformat(birthdate)
        today = date.today()

        if birth > today:
            return page(
                "خطأ - حاسبة العمر",
                "خطأ في تاريخ الميلاد.",
                """
                <div class="card">
                    <h1>تنبيه</h1>
                    <p>تاريخ الميلاد لا يمكن أن يكون في المستقبل.</p>
                    <a class="button" href="/age">العودة للحاسبة</a>
                </div>
                """
            )

        years = today.year - birth.year
        months = today.month - birth.month
        days = today.day - birth.day

        if days < 0:

            months -= 1

            if today.month == 1:
                previous_month = 12
                previous_year = today.year - 1
            else:
                previous_month = today.month - 1
                previous_year = today.year

            if previous_month in [1, 3, 5, 7, 8, 10, 12]:
                days += 31

            elif previous_month in [4, 6, 9, 11]:
                days += 30

            else:

                if (
                    previous_year % 400 == 0
                    or (
                        previous_year % 4 == 0
                        and previous_year % 100 != 0
                    )
                ):
                    days += 29
                else:
                    days += 28

        if months < 0:

            years -= 1
            months += 12

        content = f"""
        <div class="card">

            <h1>🎂 نتيجة حساب العمر</h1>

            <div class="result">

                عمرك هو:

                <br>

                <strong>
                    {years} سنة و {months} شهر و {days} يوم
                </strong>

            </div>

            <a class="button" href="/age">
                حساب عمر آخر
            </a>

            <a class="button" href="/">
                الصفحة الرئيسية
            </a>

        </div>
        """

        return page(
            "نتيجة حساب العمر - احسبني",
            "نتيجة حاسبة العمر من احسبني.",
            content
        )

    except (ValueError, TypeError):

        return "حدث خطأ في تاريخ الميلاد."


# =========================
# النسبة المئوية
# =========================
@app.route("/percentage", methods=["GET", "POST"])
def percentage():

    if request.method == "GET":

        content = """
        <div class="card">

            <h1>📊 حاسبة النسبة المئوية</h1>

            <p>
                احسب قيمة نسبة مئوية من أي رقم.
            </p>

            <form method="POST">

                <label>الرقم</label>

                <input
                    type="number"
                    name="value"
                    step="any"
                    placeholder="مثال: 500"
                    required
                >

                <label>النسبة المئوية</label>

                <input
                    type="number"
                    name="percent"
                    step="any"
                    placeholder="مثال: 20"
                    required
                >

                <button type="submit">
                    احسب النسبة
                </button>

            </form>

        </div>

        <section class="info">

            <h2>مثال على حساب النسبة المئوية</h2>

            <p>
                إذا أردت معرفة قيمة 20% من 500،
                أدخل 500 في خانة الرقم و20 في خانة النسبة.
                ستكون النتيجة 100.
            </p>

        </section>
        """

        return page(
            "حاسبة النسبة المئوية - احسبني",
            "حاسبة النسبة المئوية المجانية. احسب قيمة أي نسبة مئوية من رقم بسهولة.",
            content
        )

    try:

        value = float(request.form.get("value"))
        percent = float(request.form.get("percent"))

        result = value * percent / 100

        content = f"""
        <div class="card">

            <h1>📊 نتيجة النسبة المئوية</h1>

            <div class="result">

                {percent:g}% من {value:g}

                <br>

                <strong>
                    = {result:g}
                </strong>

            </div>

            <a class="button" href="/percentage">
                حساب جديد
            </a>

            <a class="button" href="/">
                الصفحة الرئيسية
            </a>

        </div>
        """

        return page(
            "نتيجة النسبة المئوية - احسبني",
            "نتيجة حساب النسبة المئوية.",
            content
        )

    except (ValueError, TypeError):

        return "الرجاء إدخال أرقام صحيحة."


# =========================
# الخصم
# =========================
@app.route("/discount", methods=["GET", "POST"])
def discount():

    if request.method == "GET":

        content = """
        <div class="card">

            <h1>🏷️ حاسبة الخصم</h1>

            <p>
                احسب قيمة الخصم والسعر النهائي بعد التخفيض.
            </p>

            <form method="POST">

                <label>السعر الأصلي</label>

                <input
                    type="number"
                    name="price"
                    step="any"
                    placeholder="مثال: 500"
                    required
                >

                <label>نسبة الخصم %</label>

                <input
                    type="number"
                    name="discount"
                    step="any"
                    placeholder="مثال: 20"
                    required
                >

                <button type="submit">
                    احسب الخصم
                </button>

            </form>

        </div>

        <section class="info">

            <h2>كيف تحسب السعر بعد الخصم؟</h2>

            <p>
                إذا كان السعر 500 ونسبة الخصم 20%،
                فإن قيمة الخصم تساوي 100،
                والسعر النهائي يساوي 400.
            </p>

        </section>
        """

        return page(
            "حاسبة الخصم - احسبني",
            "احسب قيمة الخصم والسعر النهائي لأي منتج باستخدام حاسبة الخصم المجانية.",
            content
        )

    try:

        price = float(request.form.get("price"))
        discount_percent = float(request.form.get("discount"))

        discount_value = price * discount_percent / 100
        final_price = price - discount_value

        content = f"""
        <div class="card">

            <h1>🏷️ نتيجة الخصم</h1>

            <div class="result">

                قيمة الخصم:
                <strong>{discount_value:g}</strong>

                <br>

                السعر بعد الخصم:
                <strong>{final_price:g}</strong>

            </div>

            <a class="button" href="/discount">
                حساب جديد
            </a>

            <a class="button" href="/">
                الصفحة الرئيسية
            </a>

        </div>
        """

        return page(
            "نتيجة الخصم - احسبني",
            "نتيجة حساب الخصم والسعر النهائي.",
            content
        )

    except (ValueError, TypeError):

        return "الرجاء إدخال أرقام صحيحة."


# =========================
# القرض
# =========================
@app.route("/loan", methods=["GET", "POST"])
def loan():

    if request.method == "GET":

        content = """
        <div class="card">

            <h1>💰 حاسبة القرض</h1>

            <p>
                احسب القسط الشهري وإجمالي المدفوعات
                وإجمالي الفائدة.
            </p>

            <form method="POST">

                <label>مبلغ القرض</label>

                <input
                    type="number"
                    name="amount"
                    step="any"
                    placeholder="مثال: 100000"
                    required
                >

                <label>نسبة الفائدة السنوية %</label>

                <input
                    type="number"
                    name="rate"
                    step="any"
                    placeholder="مثال: 5"
                    required
                >

                <label>مدة القرض بالسنوات</label>

                <input
                    type="number"
                    name="years"
                    min="1"
                    step="1"
                    placeholder="مثال: 5"
                    required
                >

                <button type="submit">
                    احسب القسط
                </button>

            </form>

        </div>

        <section class="info">

            <h2>تنبيه مهم</h2>

            <p>
                هذه الحاسبة تقديرية لأغراض الحساب فقط.
                القروض الفعلية قد تتضمن رسومًا وشروطًا
                وتكاليف إضافية تختلف حسب الجهة الممولة.
            </p>

        </section>
        """

        return page(
            "حاسبة القرض - احسبني",
            "حاسبة القروض المجانية لحساب القسط الشهري وإجمالي المدفوعات والفائدة.",
            content
        )

    try:

        amount = float(request.form.get("amount"))
        annual_rate = float(request.form.get("rate"))
        years = int(request.form.get("years"))

        if amount <= 0 or years <= 0 or annual_rate < 0:
            return "الرجاء إدخال بيانات صحيحة."

        months = years * 12
        monthly_rate = annual_rate / 100 / 12

        if monthly_rate == 0:

            monthly_payment = amount / months

        else:

            monthly_payment = (
                amount
                * monthly_rate
                * (1 + monthly_rate) ** months
                / ((1 + monthly_rate) ** months - 1)
            )

        total_payment = monthly_payment * months
        total_interest = total_payment - amount

        content = f"""
        <div class="card">

            <h1>💰 نتيجة القرض</h1>

            <div class="result">

                القسط الشهري:
                <strong>{monthly_payment:,.2f}</strong>

                <br>

                إجمالي المبلغ:
                <strong>{total_payment:,.2f}</strong>

                <br>

                إجمالي الفائدة:
                <strong>{total_interest:,.2f}</strong>

            </div>

            <a class="button" href="/loan">
                حساب جديد
            </a>

            <a class="button" href="/">
                الصفحة الرئيسية
            </a>

        </div>
        """

        return page(
            "نتيجة حاسبة القرض - احسبني",
            "نتيجة حساب القسط الشهري وإجمالي تكلفة القرض.",
            content
        )

    except (ValueError, TypeError, ZeroDivisionError):

        return "الرجاء إدخال بيانات القرض بشكل صحيح."


# =========================
# تحويل الوحدات
# =========================
@app.route("/units", methods=["GET", "POST"])
def units():

    if request.method == "GET":

        content = """
        <div class="card">

            <h1>🔄 تحويل الوحدات</h1>

            <p>
                حوّل بين وحدات الطول والوزن ودرجة الحرارة.
            </p>

            <form method="POST">

                <label>القيمة</label>

                <input
                    type="number"
                    name="value"
                    step="any"
                    placeholder="مثال: 100"
                    required
                >

                <label>نوع التحويل</label>

                <select name="conversion">

                    <option value="km_miles">
                        كيلومتر → ميل
                    </option>

                    <option value="miles_km">
                        ميل → كيلومتر
                    </option>

                    <option value="kg_lb">
                        كيلوغرام → رطل
                    </option>

                    <option value="lb_kg">
                        رطل → كيلوغرام
                    </option>

                    <option value="meter_feet">
                        متر → قدم
                    </option>

                    <option value="feet_meter">
                        قدم → متر
                    </option>

                    <option value="celsius_fahrenheit">
                        مئوية → فهرنهايت
                    </option>

                    <option value="fahrenheit_celsius">
                        فهرنهايت → مئوية
                    </option>

                </select>

                <button type="submit">
                    تحويل
                </button>

            </form>

        </div>

        <section class="info">

            <h2>تحويل الوحدات بسهولة</h2>

            <p>
                تساعدك هذه الأداة على إجراء تحويلات شائعة
                في الطول والوزن ودرجة الحرارة بسرعة.
            </p>

        </section>
        """

        return page(
            "تحويل الوحدات - احسبني",
            "أداة مجانية لتحويل وحدات الطول والوزن ودرجة الحرارة.",
            content
        )

    try:

        value = float(request.form.get("value"))
        conversion = request.form.get("conversion")

        conversions = {

            "km_miles": (
                value * 0.621371,
                "كيلومتر",
                "ميل"
            ),

            "miles_km": (
                value * 1.609344,
                "ميل",
                "كيلومتر"
            ),

            "kg_lb": (
                value * 2.2046226218,
                "كيلوغرام",
                "رطل"
            ),

            "lb_kg": (
                value * 0.45359237,
                "رطل",
                "كيلوغرام"
            ),

            "meter_feet": (
                value * 3.280839895,
                "متر",
                "قدم"
            ),

            "feet_meter": (
                value * 0.3048,
                "قدم",
                "متر"
            ),

            "celsius_fahrenheit": (
                value * 9 / 5 + 32,
                "درجة مئوية",
                "فهرنهايت"
            ),

            "fahrenheit_celsius": (
                (value - 32) * 5 / 9,
                "فهرنهايت",
                "درجة مئوية"
            )

        }

        result, from_unit, to_unit = conversions[conversion]

        content = f"""
        <div class="card">

            <h1>🔄 نتيجة التحويل</h1>

            <div class="result">

                {value:g} {from_unit}

                <br>

                =

                <br>

                <strong>
                    {result:g} {to_unit}
                </strong>

            </div>

            <a class="button" href="/units">
                تحويل جديد
            </a>

            <a class="button" href="/">
                الصفحة الرئيسية
            </a>

        </div>
        """

        return page(
            "نتيجة تحويل الوحدات - احسبني",
            "نتيجة تحويل الوحدات.",
            content
        )

    except (ValueError, TypeError, KeyError):

        return "الرجاء إدخال قيمة صحيحة."


# =========================
# BMI
# =========================
@app.route("/bmi", methods=["GET", "POST"])
def bmi():

    if request.method == "GET":

        content = """
        <div class="card">

            <h1>⚖️ حاسبة مؤشر كتلة الجسم BMI</h1>

            <p>
                أدخل الوزن والطول لحساب مؤشر كتلة الجسم.
            </p>

            <form method="POST">

                <label>الوزن بالكيلوغرام</label>

                <input
                    type="number"
                    name="weight"
                    step="any"
                    placeholder="مثال: 75"
                    required
                >

                <label>الطول بالسنتيمتر</label>

                <input
                    type="number"
                    name="height"
                    step="any"
                    placeholder="مثال: 175"
                    required
                >

                <button type="submit">
                    احسب BMI
                </button>

            </form>

        </div>

        <section class="info">

            <h2>ما هو مؤشر كتلة الجسم؟</h2>

            <p>
                مؤشر كتلة الجسم BMI هو مقياس حسابي يعتمد
                على الوزن والطول ويستخدم كأحد المؤشرات العامة
                المتعلقة بوزن الجسم.
            </p>

            <p>
                النتيجة لا تعتبر تشخيصًا طبيًا ولا تغني عن
                استشارة المختص عند الحاجة.
            </p>

        </section>
        """

        return page(
            "حاسبة مؤشر كتلة الجسم BMI - احسبني",
            "احسب مؤشر كتلة الجسم BMI باستخدام الوزن والطول.",
            content
        )

    try:

        weight = float(request.form.get("weight"))
        height_cm = float(request.form.get("height"))

        if weight <= 0 or height_cm <= 0:
            return "الرجاء إدخال الوزن والطول بشكل صحيح."

        height_m = height_cm / 100

        bmi_value = weight / (height_m ** 2)

        if bmi_value < 18.5:
            category = "نقص في الوزن"

        elif bmi_value < 25:
            category = "وزن طبيعي"

        elif bmi_value < 30:
            category = "زيادة في الوزن"

        else:
            category = "سمنة"

        content = f"""
        <div class="card">

            <h1>⚖️ نتيجة BMI</h1>

            <div class="result">

                مؤشر كتلة الجسم:

                <br>

                <strong>
                    {bmi_value:.1f}
                </strong>

                <br><br>

                التصنيف:

                <br>

                <strong>
                    {category}
                </strong>

            </div>

            <p>
                هذه النتيجة تقديرية وليست تشخيصًا طبيًا.
            </p>

            <a class="button" href="/bmi">
                حساب جديد
            </a>

            <a class="button" href="/">
                الصفحة الرئيسية
            </a>

        </div>
        """

        return page(
            "نتيجة مؤشر كتلة الجسم BMI - احسبني",
            "نتيجة حساب مؤشر كتلة الجسم BMI.",
            content
        )

    except (ValueError, TypeError, ZeroDivisionError):

        return "الرجاء إدخال الوزن والطول بشكل صحيح."


# =========================
# من نحن
# =========================
@app.route("/about")
def about():

    content = """
    <div class="card">

        <h1>من نحن</h1>

        <p>
            مرحبًا بك في احسبني، موقع عربي يهدف إلى تقديم
            حاسبات وأدوات بسيطة ومجانية للاستخدام اليومي.
        </p>

        <p>
            نعمل على تطوير أدوات سهلة الفهم وسريعة الاستخدام،
            مع التركيز على اللغة العربية وتجربة المستخدم.
        </p>

        <h2>هدفنا</h2>

        <p>
            هدفنا هو توفير أدوات حسابية عملية تساعد المستخدم
            على الوصول إلى النتيجة التي يحتاجها بأقل عدد ممكن
            من الخطوات.
        </p>

        <h2>ماذا نقدم؟</h2>

        <p>
            نقدم مجموعة من الحاسبات تشمل العمر،
            النسب المئوية، الخصومات، القروض،
            تحويل الوحدات ومؤشر كتلة الجسم.
        </p>

    </div>
    """

    return page(
        "من نحن - احسبني",
        "تعرف على موقع احسبني وأهدافه.",
        content
    )


# =========================
# تواصل معنا
# =========================
@app.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == "POST":

        name = request.form.get("name", "").strip()
        message = request.form.get("message", "").strip()

        if not name or not message:

            return "الرجاء تعبئة جميع الحقول."

        safe_name = quote(name)

        content = f"""
        <div class="card">

            <h1>شكرًا لك</h1>

            <p>
                شكرًا {safe_name} على تواصلك معنا.
            </p>

            <p>
                تم استلام رسالتك في نموذج الموقع.
            </p>

            <a class="button" href="/">
                العودة للرئيسية
            </a>

        </div>
        """

        return page(
            "تم إرسال الرسالة - احسبني",
            "صفحة تأكيد التواصل مع احسبني.",
            content
        )

    content = """
    <div class="card">

        <h1>تواصل معنا</h1>

        <p>
            إذا كان لديك اقتراح أو ملاحظة حول الموقع،
            يمكنك استخدام النموذج التالي.
        </p>

        <form method="POST">

            <label>الاسم</label>

            <input
                type="text"
                name="name"
                required
            >

            <label>رسالتك</label>

            <textarea
                name="message"
                required
            ></textarea>

            <button type="submit">
                إرسال
            </button>

        </form>

    </div>
    """

    return page(
        "تواصل معنا - احسبني",
        "تواصل مع فريق احسبني وأرسل اقتراحاتك وملاحظاتك.",
        content
    )


# =========================
# سياسة الخصوصية
# =========================
@app.route("/privacy")
def privacy():

    content = """
    <div class="card">

        <h1>سياسة الخصوصية</h1>

        <p>
            نحن نحترم خصوصية زوار موقع احسبني.
            توضح هذه الصفحة بشكل مبسط كيفية التعامل
            مع المعلومات عند استخدام الموقع.
        </p>

        <h2>المعلومات التي نقدمها</h2>

        <p>
            معظم الحاسبات الموجودة في الموقع تعمل على البيانات
            التي يدخلها المستخدم بهدف إجراء الحساب المطلوب.
        </p>

        <h2>ملفات تعريف الارتباط</h2>

        <p>
            قد يستخدم الموقع في المستقبل خدمات خارجية مثل
            أدوات التحليل أو الإعلانات، وقد تستخدم هذه الخدمات
            ملفات تعريف الارتباط وفق سياساتها الخاصة.
        </p>

        <h2>الإعلانات</h2>

        <p>
            قد يعرض الموقع إعلانات من مزودي إعلانات خارجيين.
            عند تفعيل الإعلانات مستقبلًا، سيتم التعامل معها
            وفق سياسات مزود الإعلانات والقوانين المعمول بها.
        </p>

        <h2>التحديثات</h2>

        <p>
            قد يتم تحديث سياسة الخصوصية عند إضافة خدمات أو
            ميزات جديدة إلى الموقع.
        </p>

    </div>
    """

    return page(
        "سياسة الخصوصية - احسبني",
        "سياسة الخصوصية الخاصة بموقع احسبني.",
        content
    )


# =========================
# شروط الاستخدام
# =========================
@app.route("/terms")
def terms():

    content = """
    <div class="card">

        <h1>شروط الاستخدام</h1>

        <h2>الاستخدام</h2>

        <p>
            يمكنك استخدام أدوات احسبني للأغراض الشخصية
            والتعليمية والحسابات اليومية.
        </p>

        <h2>دقة النتائج</h2>

        <p>
            نحاول تقديم نتائج حسابية دقيقة، ولكن يجب اعتبار
            النتائج معلومات تقديرية في الحالات التي تعتمد
            على افتراضات أو بيانات خارجية.
        </p>

        <h2>القروض والقرارات المالية</h2>

        <p>
            نتائج حاسبة القرض لأغراض تقديرية فقط ولا تمثل
            عرضًا ماليًا أو استشارة مالية.
        </p>

        <h2>المعلومات الصحية</h2>

        <p>
            نتائج مؤشر كتلة الجسم لا تعتبر تشخيصًا طبيًا
            ولا تغني عن استشارة المختص.
        </p>

        <h2>التحديثات</h2>

        <p>
            قد نقوم بتعديل الأدوات أو الشروط أو إضافة خدمات
            جديدة من وقت لآخر.
        </p>

    </div>
    """

    return page(
        "شروط الاستخدام - احسبني",
        "شروط استخدام موقع احسبني وحاسباته وأدواته.",
        content
    )


# =========================
# robots.txt
# =========================
@app.route("/robots.txt")
def robots():

    content = f"""
User-agent: *
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
"""

    return Response(
        content.strip(),
        mimetype="text/plain"
    )


# =========================
# sitemap.xml
# =========================
@app.route("/sitemap.xml")
def sitemap():

    pages = [
        "/",
        "/age",
        "/percentage",
        "/discount",
        "/loan",
        "/units",
        "/bmi",
        "/about",
        "/contact",
        "/privacy",
        "/terms"
    ]

    xml = '<?xml version="1.0" encoding="UTF-8"?>'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'

    for path in pages:

        xml += f"""
        <url>
            <loc>{SITE_URL}{path}</loc>
        </url>
        """

    xml += "</urlset>"

    return Response(
        xml,
        mimetype="application/xml"
    )


# =========================
# تشغيل الموقع
# =========================
if __name__ == "__main__":
    app.run(debug=True)
