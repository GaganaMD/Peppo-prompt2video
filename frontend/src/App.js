import React, { useState } from "react";
const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;

export default function App() {
  const [prompt, setPrompt] = useState("");
  const [videoUrl, setVideoUrl] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");
  const [duration, setDuration] = useState(5);

  const handleGenerate = async () => {
    setError(""); setSuccess(""); setVideoUrl("");
    if (prompt.trim().length < 3) {
      setError("Prompt must be at least 3 characters."); return;
    }
    setLoading(true);
    try {
      const response = await fetch(`${BACKEND_URL}/generate`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt, duration }),
      });
      const data = await response.json();
      if (data.video_url) {
        setVideoUrl(data.video_url);
        setSuccess(data.message || "Video generated successfully!");
      } else {
        setError(data.message || "Failed to generate video.");
      }
    } catch (e) {
      setError("Network or server error.");
    }
    setLoading(false);
  };

  return (
    <div style={{
      maxWidth: 480, margin: "40px auto", padding: 20,
      borderRadius: 6, boxShadow: "0 2px 16px #eee"
    }}>
      <h2 style={{color: "#FF7F2F"}}>AI Video Generator 🎬</h2>
      <label>Describe your video prompt:</label>
      <textarea
        value={prompt}
        onChange={e => setPrompt(e.target.value)}
        placeholder="E.g. 'A city skyline at sunrise'"
        rows={3}
        style={{ width: "100%", marginBottom: 10, borderRadius: 4, padding: 8, border:"1px solid #FF7F2F" }}
      />
      <div>
        <label>Duration (seconds):</label>
        <input
          type="number"
          min={5}
          max={10}
          value={duration}
          onChange={e => setDuration(Number(e.target.value))}
          style={{ width: 60, marginLeft: 8 }}
        />
      </div>
      <button
        onClick={handleGenerate} disabled={loading}
        style={{
          padding: "9px 20px", marginTop: 12,
          background: "#FF7F2F", color: "white",
          border: "none", borderRadius: 4, cursor: "pointer"
        }}
      >
        {loading ? "Generating..." : "Generate Video"}
      </button>
      {videoUrl && (
        <div style={{ marginTop: 20 }}>
          <video src={videoUrl} controls style={{
            width: "100%", maxHeight: 320, borderRadius: 4, boxShadow: "0 1px 8px #ccc"
          }} />
          <a href={videoUrl} download="generated-video.mp4"
            style={{ marginTop: 8, color: "#FF7F2F", textDecoration: "underline", display: "block", textAlign: "center" }}>Download Video</a>
          <button
            onClick={handleGenerate}
            style={{
              padding: "6px 18px", marginTop: 10,
              background: "#eee", color: "#FF7F2F",
              border: "none", borderRadius: 4, cursor: "pointer"
            }}
          >Regenerate</button>
        </div>
      )}
      {success && <div style={{color: "#090", margin:"14px 0 0"}}>{success}</div>}
      {error && (
        <div style={{color:"#b11", marginTop:16}}>
          {error}
          <div style={{marginTop:8}}>
            <video src="/placeholder.mp4" controls style={{width:"100%"}} />
            <div>Showing demo video as fallback.</div>
          </div>
        </div>
      )}
      {loading && <div style={{ margin: "30px auto", textAlign: "center" }}>
        <div className="loader" style={{
          display: "inline-block",
          width: 40, height: 40, borderRadius: "50%", border: "4px solid #FF7F2F", borderTop: "4px solid #fff", animation: "spin 1s linear infinite"
        }}/>
        <style>
        {`
        @keyframes spin {
          0% {transform: rotate(0deg);}
          100% {transform: rotate(360deg);}
        }
        `}
        </style>
        <div style={{ marginTop: 10 }}>Generating video, please wait...</div>
      </div>}
      <div style={{marginTop:32, fontSize:13, color:"#666"}}>
        <b>Extra features:</b> Prompt enrichment (Wikipedia context), video streaming, cache, regenerate.
      </div>
    </div>
  );
}
