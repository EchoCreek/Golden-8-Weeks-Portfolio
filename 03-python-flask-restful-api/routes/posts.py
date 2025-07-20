from flask import Blueprint, request, jsonify, current_app

# 1. 创建一个蓝图对象
# 第一个参数 'posts' 是蓝图的端点命名空间，Flask会用它来构建URL。
# 第二个参数 __name__ 是为了帮助 Flask 找到模板和静态文件的位置。
posts_bp = Blueprint('posts', __name__)

# 2. 将原来的 app.route 全部改成 posts_bp.route
# 功能：获取所有文章（GET）
@posts_bp.route("/posts", methods=["GET"])
def get_posts():
    # 在函数内部通过 current_app 获取 db
    db = current_app.db
    posts, error = db.get_all_posts()
    if error:
        return jsonify({"error": str(error)}), 500
    return jsonify(posts), 200

# 功能：创建新文章（POST）
# 接口：/posts
# 方法：POST
@posts_bp.route("/posts", methods=["POST"])
def create_post():
    # 在函数内部通过 current_app 获取 db
    db = current_app.db
    post_data = request.get_json()
    if not post_data or 'title' not in post_data or 'content' not in post_data:
        return jsonify({"error": "Missing title or content"}), 400

    title = post_data['title']
    content= post_data['content']

    new_id, error = db.create_post(title, content)
    if error:
        return jsonify({"error": str(error)}), 500

    return jsonify({"message": "Post created successfully", "id": new_id}), 201

# 功能：更新指定文章（UPDATE）
# 接口：/posts/<int:post_id>
# 方法：PUT
@posts_bp.route('/posts/<int:post_id>', methods=["PUT"])
def update_post(post_id):
    # 在函数内部通过 current_app 获取 db
    db = current_app.db
    post_data = request.get_json()
    if not post_data or 'title' not in post_data or 'content' not in post_data:
        return jsonify({"error": "Missing title or content"}), 400

    title = post_data['title']
    content = post_data['content']

    result, error = db.update_post(post_id, title, content)
    if error:
        return jsonify({"error": str(error)}), 500

    if result == 0:
        return jsonify({"error": "Post not found"}), 404

    return jsonify({"message": f"Post {post_id} updated successfully"}), 200

# 功能：删除指定文章（DELETE）
# 接口：/posts/<int:post_id>
# 方法：DELETE
@posts_bp.route('/posts/<int:post_id>', methods=["DELETE"])
def delete_post(post_id):
    # 在函数内部通过 current_app 获取 db
    db = current_app.db
    result, error = db.delete_post(post_id)
    if error:
        return jsonify({"error": str(error)}), 500

    if result == 0:
        return jsonify({"error": "Post not found"}), 404

    return jsonify({"message": f"Post {post_id} deleted successfully"}), 200