import pytube
import os
import sys
import ffmpeg

def download_yt_music(url: str) -> str:
    """
    Download music directly from the YT portal using url
    """
    output_dir="./music"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    video=pytube.YouTube(url)
    audio_stream= video.streams.filter(only_audio=True).first()
    output_file=audio_stream.download(output_path=output_dir)
    return output_file

def change_frequency_to_432(output_file: str) -> str:
    """
    Change frequency of the input file and save it to the directory
    """
    filename = f"{os.path.splitext(output_file)[0]}-432Hz.mp3"
    filter_chain = 'asetrate=44100*432/440,atempo=440/432,aresample=44100'
    if os.path.exists(filename):
        print(f"{filename} already exists")
        os.remove(output_file)
        return filename
    (
    ffmpeg
    .input(output_file)
    .output(f'{filename}', af=filter_chain)
    .run()
    )
    os.remove(output_file)
    print(f"The audio is downloaded as {filename}")
    return filename
    
def check_freq_of_mp3(file_path: str) -> None:
    """
    Check if the process succede and music has been changed to 432Hz
    """
    probe = ffmpeg.probe(file_path)
    audio_streams = [stream for stream in probe['streams'] if stream['codec_type'] == 'audio']
    
    for stream in audio_streams:
        sample_rate = stream.get('sample_rate')
        codec_name = stream.get('codec_name')
        duration = stream.get('duration')
        print(f"Sample Rate: {sample_rate}")
        print(f"Codec: {codec_name}")
        print(f"Duration: {duration}")

def main():
    """
    How to run the script: python3 main.py <url-from-yt>
    """
    
    file_downloaded = download_yt_music(sys.argv[1])
    changed_file = change_frequency_to_432(file_downloaded)
    check_freq_of_mp3(changed_file)

if __name__ == "__main__":
    main() 