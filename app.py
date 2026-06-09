import gradio as gr
from query import ask, retrieve

def handle_query(question):
    if not question.strip():
        return "Please enter a question.", "", ""
    
    result = ask(question)
    sources = "\n".join(f"• {s}" for s in result["sources"])
    
    chunks, metas, dists = retrieve(question)
    chunks_display = ""
    for i, (chunk, meta, dist) in enumerate(zip(chunks, metas, dists)):
        chunks_display += f"Chunk {i+1} (source: {meta['source']} | distance: {dist:.3f})\n"
        chunks_display += chunk + "\n"
        chunks_display += "-" * 40 + "\n"
    
    return result["answer"], sources, chunks_display

with gr.Blocks(title="UT Austin CS Professor Guide") as demo:
    gr.Markdown("# 🎓 UT Austin CS Professor Unofficial Guide")
    gr.Markdown("Ask questions about CS professors based on real student reviews.")
    
    inp = gr.Textbox(label="Your Question", placeholder="e.g. What do students say about Professor Gheith's exams?")
    btn = gr.Button("Ask", variant="primary")
    answer = gr.Textbox(label="Answer", lines=8)
    sources = gr.Textbox(label="Sources", lines=3)
    chunks_out = gr.Textbox(label="Retrieved Chunks", lines=12)
    
    btn.click(handle_query, inputs=inp, outputs=[answer, sources, chunks_out])
    inp.submit(handle_query, inputs=inp, outputs=[answer, sources, chunks_out])

demo.launch()