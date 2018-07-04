from django.shortcuts import render
from projectapp.models import Post
from github import Github
from projectapp.serializer import PostSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
import requests

class Pull_request_metadata(APIView):
    """
    Class view for get pull request metadata

    """
    def get(self, request, format=None):
        """

        :param request:  git unsername and git repository comming from request body
        :param format:  None
        :return:  Return response of custom  pull request metadata
        """
        try:
            username=request.query_params["username"]
            repo_name=request.query_params["repo_name"]
        except:
            return Response("Please send git username and repo_name")
        r = requests.get("https://api.github.com/repos/"+username+"/"+repo_name+"/pulls?state=all")
        print("Total number of pull requests: ",len(r.json()))
        pull_request=[]
        for pull_data in r.json():
            pull_request_status={}
            pull_request_status['id']=pull_data['id']
            pull_request_status['state']=pull_data['state']
            print(pull_data['merged_at'])
            if not pull_data['requested_reviewers']:
                pull_request_status['status']='REVIEWER_PENDING'
            else:
                pull_request_status['status']="REVIEW_IN_PROGRESS"
            if pull_data['merged_at']:
                pull_request_status['merge_status']='MERGED'
            else:
                pull_request_status['merge_status']='MERGE_PENDING'
            pull_request.append(pull_request_status)

        final_response={"pull_request":pull_request}

        return Response(final_response)


