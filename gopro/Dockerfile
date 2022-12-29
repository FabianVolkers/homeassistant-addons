# https://developers.home-assistant.io/docs/add-ons/configuration#add-on-dockerfile
ARG BUILD_FROM
FROM $BUILD_FROM

# Execute during the build of the image
ARG BUILD_ARCH
RUN \
    apk add --no-cache \
        ffmpeg \
        python3 \
        py3-pip

RUN pip3 install goprocam

ARG RTSP_SIMPLE_SERVER_VERSION
RUN \
    wget https://github.com/aler9/rtsp-simple-server/releases/download/${RTSP_SIMPLE_SERVER_VERSION}/rtsp-simple-server_${RTSP_SIMPLE_SERVER_VERSION}_linux_${BUILD_ARCH}.tar.gz

RUN tar -xvf rtsp-simple-server_${RTSP_SIMPLE_SERVER_VERSION}_linux_${BUILD_ARCH}.tar.gz && rm rtsp-simple-server_${RTSP_SIMPLE_SERVER_VERSION}_linux_${BUILD_ARCH}.tar.gz
RUN mv rtsp-simple-server /usr/local/bin
RUN rm rtsp-simple-server.yml LICENSE
# Copy root filesystem
COPY rootfs /

# RUN systemctl enable rtsp-simple-server
# RUN systemctl start rtsp-simple-server
# CMD ["/run.sh"]


