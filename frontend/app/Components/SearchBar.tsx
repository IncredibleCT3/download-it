"use client"

import React from 'react'
import DownloadBtn from './DownloadBtn'

const SearchBar = () => {
  const [validLink, setValidLink] = React.useState(false)

  const validateLink = (e: React.ChangeEvent<HTMLInputElement>) => {
    setValidLink(e.target.validity.valid)
  }

  return (
    <div className="flex flex-col items-center pt-10 gap-2">
      <label className="input input-lg w-100 validator">
        <svg className="h-[1em] opacity-50" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
          <g
            strokeLinejoin="round"
            strokeLinecap="round"
            strokeWidth="2.5"
            fill="none"
            stroke="currentColor"
          >
            <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path>
            <path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path>
          </g>
        </svg>
        <input
          onChange={validateLink}
          id="url-input"
          type="url"
          required
          placeholder="Enter URL"
          pattern="^(https?://)?([a-zA-Z0-9]([a-zA-Z0-9\-].*[a-zA-Z0-9])?\.)+[a-zA-Z].*$"
          title="Must be valid URL"
        />
      </label>
      <p className="validator-hint">Must be valid URL</p>
      <button className={validLink ? "btn btn-wide mb-10" : "btn btn-wide mb-10 btn-disabled"}>Download</button>
    </div>
  )
}

export default SearchBar