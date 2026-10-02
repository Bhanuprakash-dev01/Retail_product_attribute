const attributes = [
  { name: 'battery_life', value: '10 hours', status: 'INCONSISTENT', confidence: '0.90', evidence: 'Manual says up to 40 hours', action: 'Review and update' },
  { name: 'connectivity', value: 'Bluetooth', status: 'VALID', confidence: '0.96', evidence: 'Supported in spec', action: 'No action' },
  { name: 'weight', value: '250g', status: 'VALID', confidence: '0.94', evidence: 'Within expected range', action: 'No action' },
];

const workflow = [
  'Triage',
  'Product Retrieval',
  'Attribute Extraction',
  'Category Validation',
  'RAG Retrieval',
  'Attribute Validation',
  'Investigation',
  'Classification',
  'Quality Score',
  'Validation',
  'Human Approval',
  'Action',
];

export default function HomePage() {
  return (
    <main className="min-h-screen bg-slate-950 p-8 text-slate-100">
      <div className="mx-auto max-w-7xl">
        <header className="mb-6 flex items-center justify-between border-b border-slate-800 pb-4">
          <div>
            <p className="text-sm uppercase tracking-[0.2em] text-cyan-400">Retail AI Quality</p>
            <h1 className="mt-2 text-3xl font-bold">Product Attribute Quality Dashboard</h1>
          </div>
          <button className="rounded-lg bg-cyan-500 px-4 py-2 font-semibold text-slate-950">Start analysis</button>
        </header>

        <section className="grid gap-6 lg:grid-cols-[1.5fr_0.9fr]">
          <div className="rounded-2xl border border-slate-800 bg-slate-900 p-5">
            <div className="mb-4 flex gap-3">
              <input
                className="w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 text-sm"
                placeholder="Enter product ID or query"
                defaultValue="P1001"
              />
              <button className="rounded-lg border border-cyan-500 bg-cyan-500/10 px-4 py-2 text-cyan-300">Search</button>
            </div>

            <div className="mb-5 grid gap-4 md:grid-cols-3">
              <div className="rounded-xl bg-slate-950 p-4">
                <div className="text-sm text-slate-400">Product</div>
                <div className="mt-2 font-semibold">P1001</div>
              </div>
              <div className="rounded-xl bg-slate-950 p-4">
                <div className="text-sm text-slate-400">Category</div>
                <div className="mt-2 font-semibold">Headphones</div>
              </div>
              <div className="rounded-xl bg-slate-950 p-4">
                <div className="text-sm text-slate-400">Quality Score</div>
                <div className="mt-2 font-semibold text-amber-300">82.5</div>
              </div>
            </div>

            <div className="overflow-hidden rounded-xl border border-slate-800">
              <table className="min-w-full text-left text-sm">
                <thead className="bg-slate-800 text-slate-300">
                  <tr>
                    <th className="px-4 py-3">Attribute</th>
                    <th className="px-4 py-3">Value</th>
                    <th className="px-4 py-3">Status</th>
                    <th className="px-4 py-3">Confidence</th>
                    <th className="px-4 py-3">Evidence</th>
                    <th className="px-4 py-3">Action</th>
                  </tr>
                </thead>
                <tbody>
                  {attributes.map((row) => (
                    <tr key={row.name} className="border-t border-slate-800 bg-slate-900/60">
                      <td className="px-4 py-3 font-medium">{row.name}</td>
                      <td className="px-4 py-3">{row.value}</td>
                      <td className="px-4 py-3">
                        <span className={`rounded-full px-2 py-1 text-xs ${row.status === 'VALID' ? 'bg-emerald-500/15 text-emerald-300' : 'bg-amber-500/15 text-amber-300'}`}>
                          {row.status}
                        </span>
                      </td>
                      <td className="px-4 py-3">{row.confidence}</td>
                      <td className="px-4 py-3 text-slate-300">{row.evidence}</td>
                      <td className="px-4 py-3">{row.action}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>

          <aside className="space-y-6">
            <div className="rounded-2xl border border-slate-800 bg-slate-900 p-5">
              <h2 className="mb-3 text-lg font-semibold">Workflow</h2>
              <div className="space-y-2">
                {workflow.map((step, idx) => (
                  <div key={step} className={`flex items-center gap-3 rounded-lg border px-3 py-2 text-sm ${idx === 7 ? 'border-cyan-500 bg-cyan-500/10 text-cyan-200' : 'border-slate-700 bg-slate-950 text-slate-300'}`}>
                    <span className="inline-flex h-6 w-6 items-center justify-center rounded-full bg-slate-800 text-xs text-slate-300">{idx + 1}</span>
                    {step}
                  </div>
                ))}
              </div>
            </div>

            <div className="rounded-2xl border border-slate-800 bg-slate-900 p-5">
              <h2 className="mb-3 text-lg font-semibold">Human Approval</h2>
              <div className="space-y-3 text-sm text-slate-300">
                <div><span className="text-slate-500">Product:</span> P1001</div>
                <div><span className="text-slate-500">Attribute:</span> battery_life</div>
                <div><span className="text-slate-500">Current:</span> 10 hours</div>
                <div><span className="text-slate-500">Proposed:</span> 40 hours</div>
                <div className="mt-4 flex gap-2">
                  <button className="rounded-lg bg-emerald-500 px-3 py-2 font-medium text-slate-950">Approve</button>
                  <button className="rounded-lg bg-rose-500 px-3 py-2 font-medium text-white">Reject</button>
                  <button className="rounded-lg border border-slate-600 px-3 py-2">Modify</button>
                </div>
              </div>
            </div>
          </aside>
        </section>
      </div>
    </main>
  );
}
