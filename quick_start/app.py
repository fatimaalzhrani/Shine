import numpy as np
from PIL import Image
from flask import Flask, request, send_file, render_template
import io
import CSD_MT_eval

# إعداد التطبيق
app = Flask(__name__)

# الدالة لمعالجة الصور باستخدام النموذج
def get_makeup_transfer_results256(non_makeup_img, makeup_img):
    try:
        # تحويل الصور إلى مصفوفات NumPy
        non_makeup_array = np.array(non_makeup_img)
        makeup_array = np.array(makeup_img)

        # معالجة الصور باستخدام النموذج
        transfer_img = CSD_MT_eval.makeup_transfer256(non_makeup_array, makeup_array)

        # تحويل الصورة الناتجة من مصفوفة NumPy إلى صورة PIL
        transfer_img_pil = Image.fromarray(transfer_img)
        return transfer_img_pil
    except Exception as e:
        print(f"Error in processing images: {e}")
        return None

# واجهة رفع الصور
@app.route('/upload', methods=['POST'])
def upload_images():
    # التأكد من وجود الملفات المطلوبة
    if 'non_makeup' not in request.files or 'makeup' not in request.files:
        return {"error": "Please upload both images"}, 400

    try:
        # استلام الصور
        non_makeup_file = request.files['non_makeup']
        makeup_file = request.files['makeup']

        # فتح الصور مباشرة من الملفات المرفوعة
        non_makeup_img = Image.open(non_makeup_file).convert("RGB")
        makeup_img = Image.open(makeup_file).convert("RGB")

        # معالجة الصور
        result_img = get_makeup_transfer_results256(non_makeup_img, makeup_img)

        if result_img:
            # تحويل الصورة الناتجة إلى ملف Bytes لإرسالها مباشرة
            img_io = io.BytesIO()
            result_img.save(img_io, format='PNG')
            img_io.seek(0)  # إعادة المؤشر إلى بداية الملف
            return send_file(img_io, mimetype='image/png')
        else:
            return {"error": "Error processing images"}, 500

    except Exception as e:
        print(f"Error occurred: {e}")
        return {"error": "An unexpected error occurred"}, 500

# عرض الصفحة الرئيسية
@app.route('/')
def index():
    return render_template('modeltest.html')

# تشغيل التطبيق
if __name__ == '__main__':
    app.run(debug=True)