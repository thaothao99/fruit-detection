<h1><b>NHẬN DẠNG VÀ PHÂN LOẠI MỘT SỐ LOẠI TRÁI CÂY</b></h1>
<h2><b>1. Mô tả bài toán</b></h2>
<p>
Bài toán đề cập đến việc phân loại hình ảnh hoa quả, nhận dạng xem loại quả đó có tên là gì. 
  •	Input: Hình hoa quả 
  •	Output: Trả về kết quả hoa quả đó có tên là gì.
</p>
<h2><b>2. Lựa chọn phương pháp tiếp cận.</b></h2>
<p>
Bài toán được lựa chọn giải quyết theo hướng tiếp cận deep learning, cụ thể là sử dụng mô hình Convolution Neuron Network.
Lý do:
  •	Deep learning là một mô hình end-to-end, việc trích xuất các đặc trưng sẽ được thay đổi cho phù hợp với yêu cầu của bài toán.
  •	Đối với dữ liệu hình ảnh, mô hình CNN sử dụng phép convolution có thể trích xuất ra những đặt trưng tốt.
  Có nhiều mô hình CNN để lựa chọn như LeNet, GoogLenet, inception, resnet,…
Ở đây nhóm em xây dựng mô hình dựa trên mô hình VGG16 bởi những ưu điểm thực nghiệm của nó và hiệu quả trong quá trình xây dựng.
</p>
<h2><b>3. Các bước thực hiện</b></h2>
Các bước xây dựng mô hình được dựa trên phương pháp trasfer learning. Theo cách tiếp cận là fine-tuning cho phù hợp với yêu cầu của bài toán và tập dữ liệu.
Thực nghiệm được được tiến hành bằng cách sử dụng lại một pre-trained model của Inception v3, VGG16, Resnet-152 được huấn luyện trên bộ dữ liệu Image net vì tính đương đồng về đặc trưng.
<ul>
  <li><b>Bước 1: Thực hiện train dữ liệu với file Fruits_model_VGG16.ipynb trên Google Colab </b></li>
  <li><b>Bước 2: Download file model trained_vgg16.h5</b></li>
  <li><b>Bước 3: Chạy ứng dụng</b></li>
</ul>