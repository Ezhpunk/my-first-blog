from django.shortcuts import render


def post_list(reuest):
	return render(request, ' blog/post_list,html',{})
	
