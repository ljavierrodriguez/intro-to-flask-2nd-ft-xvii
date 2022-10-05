FROM gitpod/workspace-mysql:latest

RUN sudo apt-get update
RUN sudo apt-get install -y
RUN sudo apt-get install sqlite3

USER root
