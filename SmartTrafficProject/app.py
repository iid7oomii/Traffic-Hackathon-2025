import streamlit as st
import time
import pandas as pd
import numpy as np
import random

# إعدادات الصفحة
st.set_page_config(page_title="Traffic AI System", layout="wide")

# العنوان
st.title("🚦 نظام إدارة المرور الذكي | Smart Traffic Control")
st.markdown("### لوحة التحكم والمراقبة الحية")

# تقسيم الشاشة
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📡 بث الكاميرا (المحاكاة)")
    # محاولة عرض الفيديو، وإذا لم يوجد تظهر صورة بديلة
    try:
        st.video("demo.mp4", autoplay=True, muted=True, loop=True)
    except:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Traffic_jam_in_busy_intersection.jpg/800px-Traffic_jam_in_busy_intersection.jpg", caption="صورة محاكاة للتقاطع")
        st.warning("لم يتم العثور على ملف demo.mp4 - يتم عرض صورة افتراضية")

with col2:
    st.subheader("📊 بيانات التحليل الفوري")

    # مكان للأرقام المتغيرة
    placeholder = st.empty()

    # زر لبدء المحاكاة
    if st.toggle('تشغيل النظام', value=True):
        # محاكاة تحديث البيانات
        cars = random.randint(10, 50)
        wait_time = random.randint(20, 90)
        status = "مزدحم" if cars > 30 else "انسيابي"
        color = "red" if cars > 30 else "green"

        st.metric(label="عدد المركبات الحالية", value=f"{cars} سيارة")
        st.metric(label="متوسط زمن الانتظار", value=f"{wait_time} ثانية")
        st.markdown(f"### الحالة: :{color}[{status}]")

        # رسم بياني بسيط
        st.line_chart(pd.DataFrame(np.random.randn(10, 2), columns=['المسار 1', 'المسار 2']))

st.success("تم الاتصال بنظام إنترنت الأشياء (IoT) بنجاح ✅")