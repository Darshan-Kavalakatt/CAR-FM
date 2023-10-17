import React, { useEffect, useRef } from 'react';
import videojs from 'video.js';
import 'video.js/dist/video-js.css';
import Player from "video.js/dist/types/player";

const StreamComponent: React.FC = () => {
    const videoRef = useRef<HTMLVideoElement | null>(null);
    const playerRef = useRef<Player>(null as any);

    useEffect(() => {
        if (videoRef.current) {
            const initializePlayer = () => {
                const player = videojs(videoRef.current!);
                playerRef.current = player;
    
                player.src({
                    src: '/stream.m3u8',
                    type: 'application/x-mpegURL'
                });
            };
    
            // Introduce a delay before initializing the player
            const timeoutId = setTimeout(initializePlayer, 100);
    
            return () => {
                clearTimeout(timeoutId);
                if (playerRef.current) {
                    playerRef.current.dispose();
                }
            };
        }
    }, []);
    

    return (
        <div>
            <video ref={videoRef} className="video-js" controls preload="auto" width="640" height="360" />
        </div>
    );
}

export default StreamComponent;
