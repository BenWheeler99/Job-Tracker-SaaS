import './App.css';
import { useEffect, useState } from 'react';

const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || 'http://127.0.0.1:8001';

const INITIAL_FORM = {
  name: '',
  company: '',
  state: 'Applied',
  offer: false,
};

function App() {
  const [jobs, setJobs] = useState([]);
  const [form, setForm] = useState(INITIAL_FORM);
  const [editingId, setEditingId] = useState(null);
  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState('');
  const [successMessage, setSuccessMessage] = useState('');

  const resetForm = () => {
    setForm(INITIAL_FORM);
    setEditingId(null);
  };

  const fetchJobs = async () => {
    setLoading(true);
    setError('');
    try {
      const response = await fetch(`${API_BASE_URL}/jobs`);
      if (!response.ok) {
        throw new Error('Failed to load jobs.');
      }

      const data = await response.json();
      setJobs(Array.isArray(data) ? data : []);
    } catch (fetchError) {
      setError(fetchError.message || 'Unable to load jobs.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchJobs();
  }, []);

  const handleChange = (event) => {
    const { name, value, type, checked } = event.target;
    setForm((current) => ({
      ...current,
      [name]: type === 'checkbox' ? checked : value,
    }));
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    if (!form.name.trim()) {
      setError('Job title is required.');
      return;
    }

    const payload = {
      name: form.name.trim(),
      company: form.company.trim() || null,
      state: form.state,
      offer: form.offer,
    };

    const isEditing = editingId !== null;
    const endpoint = isEditing ? `${API_BASE_URL}/jobs/${editingId}` : `${API_BASE_URL}/job/`;
    const method = isEditing ? 'PUT' : 'POST';

    setSubmitting(true);
    setError('');
    setSuccessMessage('');

    try {
      const response = await fetch(endpoint, {
        method,
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload),
      });

      if (!response.ok) {
        throw new Error(`Failed to ${isEditing ? 'update' : 'create'} job.`);
      }

      await fetchJobs();
      resetForm();
      setSuccessMessage(isEditing ? 'Job updated.' : 'Job created.');
    } catch (submitError) {
      setError(submitError.message || 'Request failed.');
    } finally {
      setSubmitting(false);
    }
  };

  const handleEdit = (job) => {
    setEditingId(job.id);
    setForm({
      name: job.name || '',
      company: job.company || '',
      state: job.state || 'Applied',
      offer: Boolean(job.offer),
    });
    setSuccessMessage('');
    setError('');
  };

  const handleDelete = async (jobId) => {
    const shouldDelete = window.confirm('Delete this job?');
    if (!shouldDelete) {
      return;
    }

    setError('');
    setSuccessMessage('');

    try {
      const response = await fetch(`${API_BASE_URL}/jobs/${jobId}`, {
        method: 'DELETE',
      });

      if (!response.ok) {
        throw new Error('Failed to delete job.');
      }

      setJobs((current) => current.filter((job) => job.id !== jobId));

      if (editingId === jobId) {
        resetForm();
      }

      setSuccessMessage('Job deleted.');
    } catch (deleteError) {
      setError(deleteError.message || 'Delete request failed.');
    }
  };

  return (
    <div className="App">
      <main className="app-shell">
        <section className="app-header">
          <h1>Job Tracker Dashboard</h1>
          <p>Fast MVP frontend for your backend-driven project.</p>
        </section>

        <section className="panel form-panel">
          <h2>{editingId ? 'Edit Job' : 'Add Job'}</h2>
          <form onSubmit={handleSubmit}>
            <label htmlFor="name">Job Title</label>
            <input
              id="name"
              name="name"
              value={form.name}
              onChange={handleChange}
              placeholder="Backend Engineer"
              required
            />

            <label htmlFor="company">Company</label>
            <input
              id="company"
              name="company"
              value={form.company}
              onChange={handleChange}
              placeholder="Acme Inc."
            />

            <label htmlFor="state">Status</label>
            <select id="state" name="state" value={form.state} onChange={handleChange}>
              <option value="Applied">Applied</option>
              <option value="Rejected">Rejected</option>
              <option value="Offered">Offered</option>
            </select>

            <label className="checkbox-row" htmlFor="offer">
              <input
                id="offer"
                type="checkbox"
                name="offer"
                checked={form.offer}
                onChange={handleChange}
              />
              Offer received
            </label>

            <div className="form-actions">
              <button type="submit" disabled={submitting}>
                {submitting ? 'Saving...' : editingId ? 'Update Job' : 'Create Job'}
              </button>
              {editingId && (
                <button type="button" className="secondary" onClick={resetForm}>
                  Cancel Edit
                </button>
              )}
            </div>
          </form>
        </section>

        <section className="panel list-panel">
          <div className="list-header">
            <h2>Jobs</h2>
            <button type="button" className="secondary" onClick={fetchJobs} disabled={loading}>
              Refresh
            </button>
          </div>

          {error && <p className="status error">{error}</p>}
          {successMessage && <p className="status success">{successMessage}</p>}

          {loading ? <p>Loading jobs...</p> : null}

          {!loading && jobs.length === 0 ? (
            <p>No jobs yet. Create your first one.</p>
          ) : (
            <ul className="job-list">
              {jobs.map((job) => (
                <li key={job.id} className="job-item">
                  <div>
                    <h3>{job.name}</h3>
                    <p>{job.company || 'No company provided'}</p>
                    <p>
                      <strong>Status:</strong> {job.state} | <strong>Offer:</strong>{' '}
                      {job.offer ? 'Yes' : 'No'}
                    </p>
                  </div>
                  <div className="job-actions">
                    <button type="button" className="secondary" onClick={() => handleEdit(job)}>
                      Edit
                    </button>
                    <button type="button" className="danger" onClick={() => handleDelete(job.id)}>
                      Delete
                    </button>
                  </div>
                </li>
              ))}
            </ul>
          )}
        </section>
      </main>
    </div>
  );
}

export default App;
