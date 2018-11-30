#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
import re
import time


class DockerCmd(object):

    def get_running_docker(self):
        cmd = 'docker ps -a| grep appium'
        out = self.execute_cmd(cmd)
        for line in out.split('\n'):
            if line:
                line = line.replace('  ', '*')
                pattern = re.compile('\*+')
                line = re.split(pattern, line)
                devices = self.get_connected_devices(line[0])
                if not devices:
                    devices = 'No Device'
                yield [line[0].strip(), line[1].strip(), line[3].strip(), line[4].strip(), line[-1].strip(), devices]

    def get_connected_devices(self, docker_id):
        cmd = 'docker exec -i {} adb devices'.format(docker_id)
        out = self.execute_cmd(cmd)
        device = []
        for line in out.split('\n'):
            if line.startswith('1'):
                line = line.split('\t')[0]
                device.append(line)
        return device

    def execute_cmd(self, cmd):
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        p.wait()
        return p.stdout.read().decode('utf-8')

    def start_container(self, docker_id):
        cmd = 'docker start {}'.format(docker_id)
        self.execute_cmd(cmd)

    def stop_container(self, docker_id):
        cmd = 'docker stop {}'.format(docker_id)
        self.execute_cmd(cmd)

    def show_container_logs(self, container_id):
        cmd = 'docker logs -f {}'.format(container_id)
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in iter(p.stdout.readline, ''):
            time.sleep(1)  # Don't need this just shows the text streaming
            yield line

    def get_all_devices(self):
        cmd = 'adb devices'
        out = self.execute_cmd(cmd)
        device = []
        for line in out.split('\n'):
            if line.startswith('1'):
                line = line.split('\t')[0]
                device.append(line)
        return device

    def connect_device(self, container, device_id):
        cmd = 'docker exec -i {} adb connect {}'.format(container, device_id)
        self.execute_cmd(cmd)

    def disconnect_device(self, container, device_id):
        cmd = 'docker exec -i {} adb disconnect {}'.format(container, device_id)
        self.execute_cmd(cmd)


if __name__ == '__main__':
    docker = DockerCmd().get_all_devices()
    print(docker)
    # docker = DockerCmd().get_connected_devices('5ba5d6203970')
    # docker = DockerCmd().get_running_docker()
    # for x in docker:
    #     # x = x[0]
    #     # pattern = re.compile('\*+')
    #     # x = re.split(pattern, x)
    #     print(x)
