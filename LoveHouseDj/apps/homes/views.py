import datetime

from django import http
from django.shortcuts import render
from django.views import View

from utils.response_code import RET


class LoginViews(View):
    """
    用户登录功能
    """
    def get(self, request):
        """
        状态保持
        :param request:
        :return:
        """
        # 1、判断用户是否登录
        user = request.user
        # 2、对用户进行认证
        if not user.is_authenticated:
            return http.JsonResponse({"errno": RET.SESSIONERR, "errmsg": "用户未登录"})

        data = {
            "user_id": user.id,
            "name": user.username
        }
        return http.JsonResponse({"errno": RET.OK, "errmsg": "已登录", "data": data})

    def post(self, request):
        """
        获取用户名、密码
        :param request:
        :return:
        """
        return http.JsonResponse({"errno": RET.OK, "errmsg": "已登录"})

    def delete(self, request):
        """
        退出登录
        :param request:
        :return:
        """