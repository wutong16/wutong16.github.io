import random
import os
import glob
import json
import cv2
import numpy as np
import mmcv
import imageio


def convert_rgb_videos(video_file, save_file):
    vid = mmcv.VideoReader(video_file)
    frames = [v for v in vid]
    imageio.mimsave(save_file, frames, fps=30)

def convert_updown_leftright(video_file, save_file):
    vid = mmcv.VideoReader(video_file)
    frames = [v for v in vid]
    new_frames = []
    for f in frames:
        new_f = np.hstack([np.vstack([f[:512,:512], f[:512,512:]]), np.vstack([f[512:,:512], f[512:,512:]])])
        new_frames.append(cv2.cvtColor(new_f, cv2.COLOR_BGR2RGB))
    imageio.mimsave(save_file, new_frames, fps=30)


def combine_videos(video_file_1, video_file_2, save_file):
    vid = mmcv.VideoReader(video_file_1)
    frames_1 = [v for v in vid]

    vid = mmcv.VideoReader(video_file_2)
    frames_2 = [v for v in vid]

    frames = []
    for f1, f2 in zip(frames_1, frames_2):
        f = np.vstack([f1, f2])
        frames.append(f)
    imageio.mimsave(save_file, frames, fps=30)


dir = 'static/videos'
for file in os.listdir(dir):
    if file.startswith('example'):
        convert_updown_leftright(os.path.join(dir, file), os.path.join(dir, file[:-4] + '_new.mp4'))

exit()
dir = 'static/videos'
for file in os.listdir(dir):
    if file.startswith('cr'):
        convert_rgb_videos(os.path.join(dir, file), os.path.join(dir, file))
