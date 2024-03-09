from flask import Blueprint, render_template, flash, request, redirect, url_for
from flask_login import login_required, current_user
from . import db
from .models import Friend

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template('index.html')

@views.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/friend', methods=['POST', 'GET'])
@login_required
def add_friend():
    if request.method == 'POST':
        name = request.form.get('name')
        friend_type = request.form.get('friend_type')
        description = request.form.get('description')
        likes = request.form.get('likes')
        years = request.form.get('years')
        how_met = request.form.get('how_met')
        best_memory = request.form.get('best_memory')
        additional_info = request.form.get('addnl_info')
        new_friend = Friend(name=name, friend_type=friend_type, description=description, likes=likes, how_met=how_met, best_memory=best_memory, years=years, additional_info=additional_info, owner=current_user)
        db.session.add(new_friend)
        db.session.commit()
        flash('Friend added!', category='success')
        return redirect(url_for('views.home'))

    return render_template("friend.html", user=current_user)

@views.route('/edit_friend/<int:friend_id>', methods=['GET', 'POST'])
@login_required
def edit_friend(friend_id):
    friend = Friend.query.get_or_404(friend_id)
    if request.method == 'POST':
        friend.name = request.form.get('name')
        friend.friend_type = request.form.get('friend_type')
        friend.description = request.form.get('description')
        friend.likes = request.form.get('likes')
        friend.years = request.form.get('years')
        friend.how_met = request.form.get('how_met')
        friend.best_memory = request.form.get('best_memory')
        friend.additional_info = request.form.get('addnl_info')
        db.session.commit()
        flash('Friend updated!', category='success')
        return redirect(url_for('views.home'))

    return render_template("edit_friend.html", user=current_user, friend=friend)

@views.route('/delete_friend/<int:friend_id>', methods=['POST'])
@login_required
def delete_friend(friend_id):
    friend = Friend.query.get_or_404(friend_id)
    db.session.delete(friend)
    db.session.commit()
    flash('Friend deleted!', category='success')
    return redirect(url_for('views.home'))
