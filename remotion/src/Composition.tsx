import React from "react";
import {
  AbsoluteFill,
  Audio,
  Composition,
  Easing,
  Img,
  interpolate,
  Sequence,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";

const FPS = 30;
const WIDTH = 1080;
const HEIGHT = 1920;
const DURATION_SECONDS = 43;
const HERO_IMAGE = "assets/objectif70-grossout-gym-hero.png";

type Scene = {
  id: string;
  from: number;
  duration: number;
  speaker: string;
  title: string;
  subtitle: string;
  audio: string;
  crop: {
    startScale: number;
    endScale: number;
    x: number;
    y: number;
  };
  badge: string;
  tint: string;
};

const scenes: Scene[] = [
  {
    id: "s01_hook",
    from: 0,
    duration: 2.5,
    speaker: "Ananas Prime",
    title: "DEJA SOUILLE",
    subtitle: "POV : premiere seance,\nMangolo transpire deja.",
    audio: "voices/episode-001-v3-s01_hook-host.mp3",
    crop: { startScale: 1.0, endScale: 1.08, x: 0, y: -20 },
    badge: "OBJECTIF 70",
    tint: "rgba(255, 206, 84, 0.22)",
  },
  {
    id: "s02_machine",
    from: 2.5,
    duration: 4.5,
    speaker: "Mangolo",
    title: "LA MACHINE LE JUGE",
    subtitle: "P*tain, le tapis me regarde.\nCette machine me juge.",
    audio: "voices/episode-001-v3-s02_machine-candidate_4.mp3",
    crop: { startScale: 1.08, endScale: 1.2, x: 0, y: -80 },
    badge: "PANIC MODE",
    tint: "rgba(255, 82, 64, 0.18)",
  },
  {
    id: "s03_roast",
    from: 7,
    duration: 4,
    speaker: "Citronel",
    title: "C'EST UNE PLAINTE",
    subtitle: "Trois secondes et il demande un avocat.\nC'est pas du cardio, c'est une plainte.",
    audio: "voices/episode-001-v3-s03_roast-candidate_5.mp3",
    crop: { startScale: 1.2, endScale: 1.34, x: -80, y: -30 },
    badge: "LA VILLA CHAMBRE",
    tint: "rgba(120, 67, 255, 0.2)",
  },
  {
    id: "s04_coach",
    from: 11,
    duration: 4,
    speaker: "Coach Broco",
    title: "FUITE DE DIGNITE",
    subtitle: "Respire. Le tapis te poursuit pas,\ntu fuis la dignite.",
    audio: "voices/episode-001-v3-s04_coach-coach.mp3",
    crop: { startScale: 1.28, endScale: 1.42, x: -140, y: -140 },
    badge: "RESPECTE LA MACHINE",
    tint: "rgba(70, 221, 143, 0.2)",
  },
  {
    id: "s05_peachea",
    from: 15,
    duration: 4,
    speaker: "Peachea",
    title: "SAUCE SUR LA RAMPE",
    subtitle: "Il a mis de la sauce sur la rampe.\nLe tapis a glisse dans sa honte.",
    audio: "voices/episode-001-v3-s05_peachea-candidate_1.mp3",
    crop: { startScale: 1.22, endScale: 1.36, x: 130, y: -90 },
    badge: "DEGOUT DE LA VILLA",
    tint: "rgba(255, 236, 112, 0.2)",
  },
  {
    id: "s06_bananito",
    from: 19,
    duration: 4,
    speaker: "Bananito",
    title: "SEANCE MIXTE",
    subtitle: "S'il transpire la frite,\nc'est une seance mixte.",
    audio: "voices/episode-001-v3-s06_bananito-candidate_2.mp3",
    crop: { startScale: 1.22, endScale: 1.38, x: 120, y: -10 },
    badge: "MAUVAISE FOI",
    tint: "rgba(255, 95, 95, 0.2)",
  },
  {
    id: "s07_confessionnal",
    from: 23,
    duration: 5,
    speaker: "Mangolo",
    title: "MON BIDE VOTE CONTRE",
    subtitle: "Je cours pas, je negocie avec mon bide.\nLui il vote contre moi.",
    audio: "voices/episode-001-v3-s07_confessionnal-candidate_4.mp3",
    crop: { startScale: 1.38, endScale: 1.52, x: 0, y: -170 },
    badge: "CONFESSIONNAL",
    tint: "rgba(255, 95, 95, 0.2)",
  },
  {
    id: "s08_serpilliere",
    from: 28,
    duration: 5,
    speaker: "Coach Broco",
    title: "SERPILLIERE",
    subtitle: "Il reste l'echauffement,\net le sol demande une serpilliere.",
    audio: "voices/episode-001-v3-s08_serpilliere-coach.mp3",
    crop: { startScale: 1.18, endScale: 1.34, x: -120, y: -120 },
    badge: "LE COACH CRAQUE",
    tint: "rgba(70, 221, 143, 0.2)",
  },
  {
    id: "s09_survet",
    from: 33,
    duration: 5,
    speaker: "Citronel",
    title: "LE SURVET ABANDONNE",
    subtitle: "Son survetement a abandonne.\nLa fermeture fait ses valises.",
    audio: "voices/episode-001-v3-s09_survet-candidate_5.mp3",
    crop: { startScale: 1.32, endScale: 1.5, x: 30, y: -220 },
    badge: "ROAST FINAL",
    tint: "rgba(255, 236, 112, 0.2)",
  },
  {
    id: "s10_cliffhanger",
    from: 38,
    duration: 5,
    speaker: "Ananas Prime",
    title: "LES ESCALIERS",
    subtitle: "La production annonce la deuxieme machine :\nles escaliers.",
    audio: "voices/episode-001-v3-s10_cliffhanger-host.mp3",
    crop: { startScale: 1.0, endScale: 1.18, x: 0, y: -30 },
    badge: "CLIFFHANGER",
    tint: "rgba(255, 95, 95, 0.2)",
  },
];

const clamp = {
  extrapolateLeft: "clamp" as const,
  extrapolateRight: "clamp" as const,
};

export const MyComposition = () => {
  return (
    <Composition
      id="Objectif70Test"
      component={Objectif70Test}
      durationInFrames={DURATION_SECONDS * FPS}
      fps={FPS}
      width={WIDTH}
      height={HEIGHT}
    />
  );
};

export const Objectif70Test: React.FC = () => {
  return (
    <AbsoluteFill style={{ background: "#060606", fontFamily: "Arial, Helvetica, sans-serif" }}>
      {scenes.map((scene) => (
        <Sequence key={scene.id} from={scene.from * FPS} durationInFrames={scene.duration * FPS}>
          <SceneLayer scene={scene} />
          <Audio src={staticFile(scene.audio)} />
        </Sequence>
      ))}
      <SeriesHud />
    </AbsoluteFill>
  );
};

const SceneLayer: React.FC<{ scene: Scene }> = ({ scene }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const progress = frame / (scene.duration * fps);
  const enter = interpolate(frame, [0, 10], [0, 1], {
    ...clamp,
    easing: Easing.bezier(0.16, 1, 0.3, 1),
  });
  const imageScale = interpolate(progress, [0, 1], [scene.crop.startScale, scene.crop.endScale], clamp);
  const shake =
    scene.id === "s02_machine" || scene.id === "s07_confessionnal"
      ? Math.sin(frame * 0.7) * 12
      : Math.sin(frame * 0.45) * 5;
  const flashOpacity = interpolate(frame, [0, 4, 12], [0.72, 0.18, 0], clamp);

  return (
    <AbsoluteFill style={{ opacity: enter, background: "#090909" }}>
      <Img
        src={staticFile(HERO_IMAGE)}
        style={{
          position: "absolute",
          width: WIDTH,
          height: HEIGHT,
          objectFit: "cover",
          scale: imageScale,
          translate: `${scene.crop.x + shake}px ${scene.crop.y}px`,
          filter: scene.id === "s03_genoux" ? "contrast(1.08) saturate(0.9)" : "contrast(1.08) saturate(1.12)",
        }}
      />
      <Vignette tint={scene.tint} />
      <div
        style={{
          position: "absolute",
          inset: 0,
          background: `rgba(255,255,255,${flashOpacity})`,
          mixBlendMode: "screen",
        }}
      />
      <TopInfo scene={scene} />
      <TitleBlock scene={scene} />
      <Subtitle text={scene.subtitle} />
      <AudioBars />
      <SceneProgress duration={scene.duration} />
    </AbsoluteFill>
  );
};

const Vignette: React.FC<{ tint: string }> = ({ tint }) => {
  return (
    <AbsoluteFill>
      <div
        style={{
          position: "absolute",
          inset: 0,
          background:
            "radial-gradient(circle at 50% 35%, rgba(0,0,0,0.05) 0%, rgba(0,0,0,0.15) 42%, rgba(0,0,0,0.74) 100%)",
        }}
      />
      <div
        style={{
          position: "absolute",
          inset: 0,
          background: `linear-gradient(180deg, rgba(0,0,0,0.42) 0%, ${tint} 42%, rgba(0,0,0,0.64) 100%)`,
          mixBlendMode: "multiply",
        }}
      />
      <div
        style={{
          position: "absolute",
          left: -140,
          right: -140,
          bottom: 0,
          height: 520,
          background: "linear-gradient(180deg, rgba(0,0,0,0) 0%, rgba(0,0,0,0.92) 64%)",
        }}
      />
    </AbsoluteFill>
  );
};

const TopInfo: React.FC<{ scene: Scene }> = ({ scene }) => {
  const frame = useCurrentFrame();
  const y = interpolate(frame, [0, 12], [-46, 0], {
    ...clamp,
    easing: Easing.bezier(0.16, 1, 0.3, 1),
  });

  return (
    <div
      style={{
        position: "absolute",
        top: 74,
        left: 64,
        right: 64,
        display: "flex",
        alignItems: "center",
        justifyContent: "space-between",
        gap: 24,
        translate: `0 ${y}px`,
      }}
    >
      <div
        style={{
          padding: "16px 22px",
          borderRadius: 8,
          background: "rgba(0,0,0,0.56)",
          border: "2px solid rgba(255,255,255,0.22)",
          color: "#fff8df",
          fontSize: 34,
          fontWeight: 1000,
          textTransform: "uppercase",
          maxWidth: 520,
          overflow: "hidden",
          textOverflow: "ellipsis",
          whiteSpace: "nowrap",
        }}
      >
        {scene.speaker}
      </div>
      <div
        style={{
          padding: "16px 20px",
          borderRadius: 8,
          background: "#ffdd4a",
          color: "#130f09",
          fontSize: 30,
          fontWeight: 1000,
          boxShadow: "0 16px 42px rgba(0,0,0,0.28)",
        }}
      >
        100 000 EUR
      </div>
    </div>
  );
};

const TitleBlock: React.FC<{ scene: Scene }> = ({ scene }) => {
  const frame = useCurrentFrame();
  const titleY = interpolate(frame, [2, 16], [38, 0], {
    ...clamp,
    easing: Easing.bezier(0.16, 1, 0.3, 1),
  });
  const titleScale = interpolate(frame, [0, 12, 28], [0.94, 1.04, 1], clamp);

  return (
    <div
      style={{
        position: "absolute",
        top: scene.id === "s01_pov" ? 230 : 265,
        left: 58,
        right: 58,
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        gap: 20,
        translate: `0 ${titleY}px`,
        scale: titleScale,
      }}
    >
      <div
        style={{
          color: "#17110b",
          background: "#fff2b4",
          borderRadius: 8,
          padding: "12px 22px",
          fontSize: 28,
          lineHeight: 1,
          fontWeight: 1000,
          textTransform: "uppercase",
          boxShadow: "0 14px 38px rgba(0,0,0,0.28)",
        }}
      >
        {scene.badge}
      </div>
      <div
        style={{
          color: "#ffffff",
          fontSize: scene.title.length > 17 ? 72 : 92,
          lineHeight: 0.94,
          fontWeight: 1000,
          textAlign: "center",
          textShadow: "0 12px 34px rgba(0,0,0,0.9), 0 3px 0 rgba(0,0,0,0.5)",
          maxWidth: 980,
        }}
      >
        {scene.title}
      </div>
    </div>
  );
};

const Subtitle: React.FC<{ text: string }> = ({ text }) => {
  const frame = useCurrentFrame();
  const y = interpolate(frame, [4, 18], [58, 0], {
    ...clamp,
    easing: Easing.bezier(0.16, 1, 0.3, 1),
  });
  const long = text.length > 78;

  return (
    <div
      style={{
        position: "absolute",
        left: 54,
        right: 54,
        bottom: 94,
        minHeight: 245,
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        borderRadius: 14,
        padding: "30px 34px",
        background: "rgba(0,0,0,0.78)",
        border: "3px solid rgba(255,255,255,0.16)",
        boxShadow: "0 28px 70px rgba(0,0,0,0.52)",
        translate: `0 ${y}px`,
      }}
    >
      <div
        style={{
          color: "#fff7d0",
          fontSize: long ? 50 : 58,
          lineHeight: 1.08,
          fontWeight: 1000,
          textAlign: "center",
          whiteSpace: "pre-line",
          textShadow: "0 5px 0 rgba(0,0,0,0.65)",
        }}
      >
        {text}
      </div>
    </div>
  );
};

const AudioBars: React.FC = () => {
  const frame = useCurrentFrame();
  return (
    <div
      style={{
        position: "absolute",
        left: 72,
        bottom: 374,
        display: "flex",
        gap: 9,
        alignItems: "end",
        height: 58,
        opacity: 0.84,
      }}
    >
      {Array.from({ length: 18 }).map((_, index) => {
        const h = 16 + Math.abs(Math.sin(frame * 0.18 + index * 0.72)) * 42;
        return (
          <div
            key={index}
            style={{
              width: 10,
              height: h,
              borderRadius: 10,
              background: index % 3 === 0 ? "#ffdc52" : index % 3 === 1 ? "#ff6e4a" : "#7de8c5",
            }}
          />
        );
      })}
    </div>
  );
};

const SceneProgress: React.FC<{ duration: number }> = ({ duration }) => {
  const frame = useCurrentFrame();
  const width = interpolate(frame, [0, duration * FPS], [0, 1], clamp);

  return (
    <div
      style={{
        position: "absolute",
        left: 0,
        right: 0,
        top: 0,
        height: 22,
        background: "rgba(255,255,255,0.12)",
      }}
    >
      <div
        style={{
          width: `${width * 100}%`,
          height: "100%",
          background: "linear-gradient(90deg, #ffdc52, #ff6e4a, #7de8c5)",
        }}
      />
    </div>
  );
};

const SeriesHud: React.FC = () => {
  return (
    <>
      <div
        style={{
          position: "absolute",
          right: 62,
          bottom: 32,
          color: "rgba(255,255,255,0.5)",
          fontSize: 24,
          fontWeight: 900,
          textTransform: "uppercase",
        }}
      >
        AIGC - TEST 03
      </div>
      <div
        style={{
          position: "absolute",
          left: 62,
          bottom: 32,
          color: "rgba(255,255,255,0.5)",
          fontSize: 24,
          fontWeight: 900,
          textTransform: "uppercase",
        }}
      >
        Objectif 70
      </div>
    </>
  );
};
