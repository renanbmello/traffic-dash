# src/utils/video_utils.py

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

def salvar_trecho_video(video_path: str, inicio: float, fim: float, output_path: str):
    """
    Salva um trecho de um vídeo.

    Args:
        video_path (str): Caminho para o vídeo original.
        inicio (float): Tempo inicial em segundos.
        fim (float): Tempo final em segundos.
        output_path (str): Caminho para salvar o vídeo cortado.
    """
    ffmpeg_extract_subclip(video_path, inicio, fim, targetname=output_path)
