import '@/app/index.css'
import React from 'react'
import { QueryClientProvider } from '@tanstack/react-query'
import { queryClient } from '@/shared/config'

export function Providers({ children }: { children: React.ReactNode }) {
  return (
    <QueryClientProvider client={queryClient}>
      {children}
    </QueryClientProvider>
  )
}
